import json
import logging
import asyncio
import aiohttp
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor

# Configure global logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def fetch_webpage_content(session, url):
    """Fetches the content of a webpage asynchronously."""
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            content = await response.read()
            return content.decode('utf-8', errors='ignore')
    except aiohttp.ClientError as e:
        logging.error(f"Failed to fetch the page: {e}")
        return None

def parse_links_from_html(html_content, base_url):
    """Extracts all links from the HTML content of a webpage."""
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a')
    return [urljoin(base_url, link['href']) for link in links if 'href' in link.attrs]

def determine_link_status(url):
    """Determines if a link is broken and returns its details."""
    try:
        response = requests.get(url, allow_redirects=True)
        if response.status_code >= 400:
            logging.info(f"Detected broken link (status code {response.status_code}): {url}")
            return {
                "url": url,
                "status_code": response.status_code,
                "reason": response.reason
            }
        # Check for common error messages in the content
        error_phrases = ["404 Not Found", "Page Not Found", "Error 404", "This page isn't available", "500 Internal Server Error", "Error 500", "Server Error"]
        text = response.text
        if any(phrase in text for phrase in error_phrases):
            logging.info(f"Detected broken link (error message found): {url}")
            return {
                "url": url,
                "status_code": response.status_code,
                "reason": "Error message found in page content"
            }
    except requests.RequestException as e:
        logging.info(f"Detected broken link: {url}")
        return {
            "url": url,
            "status_code": "N/A",
            "reason": str(e)
        }
    return None

def save_broken_links_to_json(broken_links, filename="broken_links_list.json"):
    """Saves the broken links to a JSON file."""
    with open(filename, mode='w') as file:
        json.dump(broken_links, file, indent=4)
    logging.info(f"Broken links saved to {filename}")

async def crawl_website(session, start_url, max_workers=20):
    """Crawls a website to identify broken links asynchronously using a stack to avoid deep recursion."""
    visited_urls_set = set()
    broken_links_list = []
    stack = [start_url]

    while stack:
        url = stack.pop()
        if url in visited_urls_set:
            continue

        visited_urls_set.add(url)
        webpage_content = await fetch_webpage_content(session, url)
        if not webpage_content:
            continue

        links = parse_links_from_html(webpage_content, url)
        logging.info(f"Discovered {len(links)} links on {url} for further inspection.")

        # Use ThreadPoolExecutor to check link statuses concurrently
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            loop = asyncio.get_event_loop()
            tasks = [loop.run_in_executor(executor, determine_link_status, link) for link in links]
            results = await asyncio.gather(*tasks)

        for result in results:
            if result:
                broken_links_list.append(result)

        stack.extend(link for link in links if link not in visited_urls_set and urljoin(url, '/') in link)

    return broken_links_list

async def main():
    start_url = 'https://www.google.com/'  
    
    async with aiohttp.ClientSession() as session:
        broken_links = await crawl_website(session, start_url)

    logging.info("Identified broken links:")
    if broken_links:
        for link in broken_links:
            logging.info(link)
        save_broken_links_to_json(broken_links)
    else:
        logging.info("No broken links found")

if __name__ == "__main__":
    asyncio.run(main())
