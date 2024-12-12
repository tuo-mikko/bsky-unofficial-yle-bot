import requests
import datetime

def fetch_content(url):
    """
    Fetches content from the given URL.
    
    Args:
    - url (str): The URL to fetch content from.
    
    Returns:
    - str: The HTML content of the page, or None if an error occurs.
    """
    try:
        # Simulating a simple HTTP request to fetch the content (this could be extended)
        response = requests.get(url)
        response.raise_for_status()  # Raises an error for bad responses (e.g., 404)
        print(f"Succesfully fetched {url} at {datetime.datetime.now()}")
        return response
    except requests.exceptions.RequestException as e:
        print(f"{datetime.datetime.now()} Error fetching the URL {url}: {e}")
        return None

fetch_content("https://yle.fi/uutiset/tuoreimmat")