import requests
import datetime


def fetch_content(url: str):
    """
    Fetches content from the given URL.

    Args:
    - url (str): The URL to fetch content from.

    Returns:
    - str: The HTML content of the page, None if an error occurs.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"Succesfully fetched {url} at {datetime.datetime.now()}")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"{datetime.datetime.now()} Error fetching the URL {url}: {e}")
        return None


print("Yeah")
