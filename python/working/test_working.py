from working import convert
import pytest

def main():
    test_format()
    test_hour()
    test_min()



def test_format():
    with pytest.raises(ValueError):
        convert("5 AM 9 PM")
        convert("5 AM : 9 PM")
        convert("5 AM - 9 PM")

def test_hour():
    with pytest.raises(ValueError):
        convert("5 AM to 13 PM")
        convert("13 PM to 5 AM")

def test_min():
    with pytest.raises(ValueError):
        convert("5:70 AM to 9:00 PM")
        convert("5:00 AM to 9:65 PM")

def test_output():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("8 AM to 8 AM") == "08:00 to 08:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("9:00 AM to 5:30 PM") == "09:00 to 17:30"


if __name__ == "__main__":
    main()