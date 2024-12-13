import requests, fetchHTML
from datetime import datetime
from bs4 import BeautifulSoup

def convertDate(dateinfo: str) -> datetime:
    """
    Converts a string to datetime if possible

    Args:
    - dateinfo (str): The date candidate.

    Returns:
    - datetime: The string converted into datetime, None if it cannot be done.
    """
    if not dateinfo:
        print("No date provided.")
        return None

    try:
        timestamp = datetime.fromisoformat(dateinfo.replace("Z", "+00:00"))
        return timestamp
    except ValueError as e:
        print(f"Date parsing error: {e}")
        return None
    
def parse_content(page: str) -> list:
    """
    Parse the YLE latest news page into a list of articles. If some values are missing, they are not included in the result.

    Args:
    - page (str): The HTML content of the page as a string.

    Returns:
    - List[dict]: List of articles, keys 'title' (str), 'url' (str), and 'date' (datetime).
    """
    if not page:
        return []

    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(page, "html.parser")
    article_containers = soup.find_all("div", class_="GridSystem__GridCell-sc-613a840-0 gVhexk")
    parsedArticles = []

    # Iterate through found content
    for article in article_containers:

        article_link = None
        article_text = None
        timestamp = None

        link_tag = article.find("a", class_="underlay-link visitable-link")
        if link_tag:
            article_link = link_tag['href']
            article_text = link_tag.text.strip()

        time_tag = article.find("time", class_="DateTime___StyledTime-sc-f0ffa757-0 kpZoAj")
        if time_tag and time_tag.get('datetime'):
            timestamp = convertDate(time_tag['datetime'])

        # Append to the list only if fields are valid
        if article_link and article_text and timestamp:
            parsedArticles.append({'title': article_text, 'url': article_link, 'date': timestamp})
            
    return parsedArticles