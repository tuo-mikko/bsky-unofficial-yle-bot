import pytest
from scraper import fetch_content, parse_content  # Assuming your scraper functions are in a file called scraper.py

# Test if content is fetched correctly
def test_fetch_content():
    url = "https://example.com"  # Replace with a real URL or a mock URL
    content = fetch_content(url)
    assert content is not None  # Check if content is returned

# Test if content is parsed correctly
def test_parse_content():
    html_content = "<html><body><h2 class='article-title'>Test Title</h2></body></html>"
    parsed_titles = parse_content(html_content)
    assert len(parsed_titles) == 1  # Expecting one title
    assert parsed_titles[0] == "Test Title"  # The title we expect