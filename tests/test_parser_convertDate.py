import datetime
from parser import convertDate

# These tests aim to see if the dateparser works as expected with correct input, and can handle invalid inputs as well.

# Test for valid date
def test_valid_date():
    date_str = "2024-12-12T15:52:32+0200"
    result = convertDate(date_str)
    expected = datetime.datetime(2024, 12, 12, 15, 52, 32, tzinfo=datetime.timezone(datetime.timedelta(seconds=7200)))
    assert result == expected

# Test for invalid date
def test_invalid_date():
    date_str = "invalid-date"
    result = convertDate(date_str)
    assert result is None

# Test for empty date
def test_empty_date():
    date_str = ""
    result = convertDate(date_str)
    assert result is None

# Test for None date
def test_none_date():
    date_str = None
    result = convertDate(date_str)
    assert result is None