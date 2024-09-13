import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Constants declaration
BASE_URL = "https://www.amazon.in" 
SEARCH_TERM = "lg soundbar"
MAX_WAIT_TIME = 15  
OUTPUT_FILE = "amazon_lg_soundbars.json"

# Sets up the Chrome WebDriver
def configure_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(MAX_WAIT_TIME)
    return driver

# Launches the Amazon website and conducts a search using the given keyword.
def open_amazon_and_search(driver, base_url, search_term):
    driver.get(base_url) 
    
    try:
        # Pauses until the search field is visible, inputs the keyword and sends the request
        search_box = WebDriverWait(driver, MAX_WAIT_TIME).until(
            EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search_box.send_keys(search_term) # Input keyword
        search_box.submit()# Send the search request
    except TimeoutException:
        raise Exception("Failed to locate search box within the specified time")

# Gathers product names and costs from the search results page.
def extract_product_info(driver):
    try:
        # Wait for product names and prices to be present on the page
        product_names = WebDriverWait(driver, MAX_WAIT_TIME).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.a-size-medium.a-color-base.a-text-normal"))
        )
        product_prices = WebDriverWait(driver, MAX_WAIT_TIME).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.a-price-whole"))
        )
    except TimeoutException:
        raise Exception("Failed to locate product elements within the specified time")

# List to store the product information
    products = []
    for i, product in enumerate(product_names):
        product_name = product.text.strip().lower() # Get the product name and change to lowercase
        
        try:
            # Get the price and convert it to an integer, removing commas
            price_element = product_prices[i]
            price = int(price_element.text.replace(",", ""))
        except IndexError:
            continue
        
        if "lg" in product_name:
            products.append((price, product_name))

    return products

# Sorts the list of products by price in ascending order.
def sort_products_by_price(products):
    return sorted(products, key=lambda x: x[0])

# Saves the list of products to a JSON file.
def save_products_to_json(products, file_name):
    try:
        with open(file_name, "w") as f:
            json.dump([{"price": price, "name": name} for price, name in products], f, indent=4)
        print(f"Products saved successfully to {file_name}")
    except IOError as e:
        raise Exception(f"Error saving products to JSON file: {e}")

# Prints the sorted list of products with their prices.
def print_sorted_products(products):
    for i, (price, name) in enumerate(products, start=1):
        print(f"{i}. Price: ₹{price:,}, Name: {name}")

def main():
    """
    The main function that have the entire process:
    1. Configures and initializes the WebDriver.
    2. Opens Amazon and searches for 'LG Soundbar'.
    3. Extracts product names and prices from the search results.
    4. Sorts the products by price.
    5. Saves the sorted products to a JSON file.
    6. Prints the sorted products.
    """
    driver = configure_driver() 
    
    try:
        open_amazon_and_search(driver, BASE_URL, SEARCH_TERM) 
        products = extract_product_info(driver)
        sorted_products = sort_products_by_price(products)
        save_products_to_json(sorted_products, OUTPUT_FILE) 
        print_sorted_products(sorted_products)
        
    except Exception as e:
        print(f"An error occurred: {e}")  # Handle any errors that occur during execution
    
    finally:
        driver.quit() # Ensure the browser is closed when done
        
# Execute the script
if __name__ == "__main__":
    main()
