import pytest
import requests
from unittest import mock


from fetchHTML import fetch_content

# Test for succesful fetch
def test_fetch_content_success():
    url = "https://example.com"
    html_content = "<html><body><h1>Example Domain</h1></body></html>"
    
    with mock.patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = html_content
        
        result = fetch_content(url)
        
        assert result == html_content
        mock_get.assert_called_once_with(url)


# Test for a 404 error
def test_fetch_content_404_error():
    url = "https://nonexistenturl.com"
    
    with mock.patch("requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.HTTPError("404 Client Error: Not Found")
        
        result = fetch_content(url)
        
        assert result is None
        mock_get.assert_called_once_with(url)


# Test for request timeout 
def test_fetch_content_timeout():
    url = "https://example.com"
    
    with mock.patch("requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.Timeout("The request timed out")
        
        result = fetch_content(url)
        
        assert result is None
        mock_get.assert_called_once_with(url)


# Test for request exception
def test_fetch_content_generic_error():
    url = "https://example.com"
    
    with mock.patch("requests.get") as mock_get:
        mock_get.side_effect = requests.exceptions.RequestException("Generic error")
        
        result = fetch_content(url)
        
        assert result is None
        mock_get.assert_called_once_with(url)