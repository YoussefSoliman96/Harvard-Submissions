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




if __name__ == "__main__":
    main()