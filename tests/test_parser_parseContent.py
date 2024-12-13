from parser import parse_content
import datetime

# These tests aim to see if the scraper works as expected with correct input, and can handle invalid inputs as well.
# It uses a snapshot of the actual YLE page, as well as two invalid versions.

# Function to read HTML from a file
def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Test function for valid HTML input
def test_parse_content_valid():
    
    valid_html = read_html_file('tests/validHtml.html')
    result = parse_content(valid_html)

    assert len(result) == 20 
    assert result[0]['title'] == 'Ministeri Kaisa Juuso: Oulaskankaan yöpäivystyksen lopettamista katsotaan uudelleen'
    assert result[0]['url'] == 'https://yle.fi/a/74-20131203'
    assert result[0]['date'] == datetime.datetime(2024, 12, 13, 12, 40, 36, tzinfo=datetime.timezone(datetime.timedelta(seconds=7200)))

# Test function for invalid HTML, invalid date
def test_parse_content_date_invalid():
    invalid_html = read_html_file('tests/invalidHtmlDate.html')

    result = parse_content(invalid_html)

    assert len(result) == 0 


# Test function for incompatible HTML with elements missing
def test_parse_content_incompatible():
    incompatible_html = read_html_file('tests/invalidHtmlElements.html')
    result = parse_content(incompatible_html)
    assert len(result) == 0