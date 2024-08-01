import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
import logging

# Configure global logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_page_content(url):
    """Fetches the content of a webpage."""
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        logging.error(f"Failed to fetch the page: {e}")
        return None
    return response.text

def extract_image_urls(html_content, base_url):
    """Extracts image URLs from the HTML content of a webpage."""
    soup = BeautifulSoup(html_content, 'html.parser')
    images = soup.find_all('img')
    img_urls = [urljoin(base_url, img['src']) for img in images if 'src' in img.attrs]
    return img_urls

def check_if_image_is_broken(image_url):
    """Checks if an image is broken."""
    try:
        response = requests.get(image_url, stream=True)
        if response.status_code!= 200:
            logging.info(f"Image is broken: {image_url}")
            return image_url
    except requests.RequestException:
        logging.info(f"Image is broken: {image_url}")
        return image_url
    return None

def process_images(page_url):
    """Processes images from a given page URL."""
    html_content = fetch_page_content(page_url)
    if html_content:
        img_urls = extract_image_urls(html_content, page_url)
        logging.info(f"Found {len(img_urls)} images. Checking for broken images...")
        
        broken_images = []
        with ThreadPoolExecutor(max_workers=10) as executor:
            results = executor.map(check_if_image_is_broken, img_urls)
            for result in results:
                if result:
                    broken_images.append(result)

        if broken_images:
            logging.info("Broken images found:")
            for img_url in broken_images:
                logging.info(img_url)
        else:
            logging.info("No broken images found.")
    else:
        logging.info("Failed to fetch the page content.")

def main():
    page_url = 'https://the-internet.herokuapp.com/broken_images'
    process_images(page_url)

if __name__ == "__main__":
    main()
