import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
import logging

# Configure global logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_webpage_content(url):
    """Fetches the content of a webpage."""
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Failed to fetch the page: {e}")
        return None
    return response.text

def parse_links_from_html(html_content, base_url):
    """Extracts all links from the HTML content of a webpage."""
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a')
    return [urljoin(base_url, link['href']) for link in links if 'href' in link.attrs]

def determine_link_status(url):
    """Determines if a link is broken."""
    try:
        response = requests.head(url, allow_redirects=True)
        if response.status_code >= 400:
            logging.info(f"Detected broken link: {url}")
            return url
    except requests.RequestException:
        logging.info(f"Detected broken link: {url}")
        return url
    return None

def crawl_website_recursively(url, visited_urls_set, broken_links_set):
    """Recursively crawls a website to identify broken links."""
    if url in visited_urls_set:
        return

    visited_urls_set.add(url)
    webpage_content = fetch_webpage_content(url)
    if not webpage_content:
        return

    links = parse_links_from_html(webpage_content, url)
    logging.info(f"Discovered {len(links)} links on {url} for further inspection.")

    with ThreadPoolExecutor(max_workers=10) as executor:
        broken_links = executor.map(determine_link_status, links)
        for broken_link in broken_links:
            if broken_link:
                broken_links_set.add(broken_link)

    for link in links:
        if link not in visited_urls_set and urljoin(url, '/') in link:
            crawl_website_recursively(link, visited_urls_set, broken_links_set)

def main():
    start_url = 'https://www.wikipedia.org/'
    visited_urls = set()
    broken_links = set()
    crawl_website_recursively(start_url, visited_urls, broken_links)

    logging.info("Identified broken links:")
    for link in broken_links:
        logging.info(link)
    else:
        logging.info("No broken links found")



if __name__ == "__main__":
    main()
