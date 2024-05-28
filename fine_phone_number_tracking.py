import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
import folium
import argparse
import os
from colorama import init, Fore
from opencage.geocoder import OpenCageGeocode
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variables
OPENCAGE_API_KEY = "OPENCAGE_API_KEY"

# Initialize colorama for colored output
init()

def process_number(phone_number):
    """Attempts to parse and analyze a phone number."""
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number)
        
        # Format the phone number in international format
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        print(f"{Fore.GREEN}[+] Analyzing {formatted_number}..")

        # Get the region information
        region = phonenumbers.region_code_for_number(parsed_number)
        print(f"{Fore.GREEN}[+] Region: {region if region else Fore.RED}[-] Unknown")

        # Get the timezone information
        time_zones = timezone.time_zones_for_number(parsed_number)
        print(f"{Fore.GREEN}[+] Time Zone: {time_zones[0] if time_zones else Fore.RED}[-] Unknown")

        # Get the geolocation information
        location = geocoder.description_for_number(parsed_number, "en")
        print(f"{Fore.GREEN}[+] Location: {location if location else Fore.RED}[-] Unknown")

        # Get the service provider information
        service_provider = carrier.name_for_number(parsed_number, "en")
        print(f"{Fore.GREEN}[+] Service Provider: {service_provider if service_provider else Fore.RED}[-] Unknown")

    except phonenumbers.phonenumberutil.NumberParseException:
        print(f"{Fore.RED}[-] Invalid phone number or network issue.")
        exit(1)


def get_approx_coordinates(location):
    """Finds approximate geographical coordinates for a given location."""
    try:
        # Initialize the geocoder with the API key
        geocoder = OpenCageGeocode(OPENCAGE_API_KEY)
        
        # Make a request to the geocoding API
        results = geocoder.geocode(location)
        
        # Check if the API returned any results
        if results:
            # Extract latitude and longitude from the first result
            latitude, longitude = results[0]['geometry']['lat'], results[0]['geometry']['lng']
            print(f"[+] Latitude: {latitude}, Longitude: {longitude}")

            # Reverse geocode the coordinates to get the address
            address = geocoder.reverse_geocode(latitude, longitude)
            if address:
                address = address[0]['formatted']
                print(f"{Fore.LIGHTRED_EX}[+] Approximate Address: {address}")
            else:
                print(f"{Fore.RED}[-] No address found for the given coordinates.")
            
            return latitude, longitude
        else:
            print(f"{Fore.RED}[-] No results found for the location.")
            return None, None

    except Exception as e:
        print(f"{Fore.RED}[-] Error getting location: {str(e)}")
        return None, None


def draw_map(location, latitude, longitude):
    """Creates and saves a map centered around the given coordinates."""
    try:
        # Create a folium map centered around the coordinates
        my_map = folium.Map(location=[latitude, longitude], zoom_start=9)
        
        # Add a marker to the map at the specified location
        folium.Marker([latitude, longitude], popup=location).add_to(my_map)
        
        # Save the map as an HTML file
        cleaned_phone_number = clean_phone_number(location)
        file_name = f"{cleaned_phone_number}.html"
        my_map.save(file_name)
        print(f"[+] Map saved as {os.path.abspath(file_name)}")

    except Exception as e:
        print(f"{Fore.RED}[-] Error drawing map: {str(e)}")

def clean_phone_number(phone_number):
    """Removes non-digit characters from a phone number."""
    return ''.join(char for char in phone_number if char.isdigit() or char == '+') or "unknown"

def parse_arguments():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description="Track the approximate location of a phone number.")
    parser.add_argument("phone_number", type=str, help="Phone number to track, including country code.")
    return parser.parse_args()

def check_internet_connection():
    """Checks if there is an active internet connection."""
    try:
        # Send a GET request to a known website (e.g., Google)
        response = requests.get("https://www.google.com", timeout=5)
        # Check if the response status code is 200, indicating a successful connection
        if response.status_code == 200:
            return True
    except requests.ConnectionError:
        pass
    return False

def main():
    # Parse command-line arguments
    args = parse_arguments()
    
    # Check internet connection before proceeding
    if not check_internet_connection():
        print("No internet connection. Please check your network settings.")
        exit(1)

    # Process phone number, get coordinates, and draw map
    process_number(args.phone_number)
    latitude, longitude = get_approx_coordinates(args.phone_number)
    
    # Check if valid coordinates are available
    if latitude is not None and longitude is not None:
        draw_map(args.phone_number, latitude, longitude)
    else:
        print(f"{Fore.RED}[-] Unable to draw map due to missing coordinates.")

if __name__ == "__main__":
    main()
