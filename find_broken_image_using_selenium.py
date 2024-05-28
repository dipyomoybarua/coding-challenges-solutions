from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

def get_image_urls(page_url):
    """
    Uses Selenium to fetch all image URLs from the given webpage URL.
    """
    # Initialize the WebDriver 
    driver = webdriver.Chrome()  
    driver.get(page_url)

    # Find all image elements on the page
    image_elements = driver.find_elements(By.TAG_NAME, 'img')
    img_urls = [img.get_attribute('src') for img in image_elements]

    driver.quit()  # Close the browser
    return img_urls

def is_image_broken(img_url):
    """
    Checks if the image at the given URL is broken.
    """
    try:
        response = requests.get(img_url, stream=True)
        if response.status_code != 200:
            return img_url
    except requests.RequestException:
        return img_url
    return None

def main():
    page_url = 'https://the-internet.herokuapp.com/broken_images'
    img_urls = get_image_urls(page_url)
    print(f"Found {len(img_urls)} images. Checking for broken images...")

    broken_images = [img_url for img_url in img_urls if is_image_broken(img_url)]

    if broken_images:
        print("Broken images found:")
        for img_url in broken_images:
            print(img_url)
    else:
        print("No broken images found.")

if __name__ == "__main__":
    main()
