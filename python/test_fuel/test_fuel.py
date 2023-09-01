from fuel import convert
from fuel import gauge
import pytest

def main():
    test_convert()
    test_division()
    test_value()

def test_convert():
    assert convert("1/2") == 50 and gauge(50) == "50%"
    assert convert("1/100") == 1 and gauge(1) == "E"
    assert convert("99/100") == 99 and gauge(99) == "F"


def test_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value():
    with pytest.raises(ValueError):
        convert("d/c")

if __name__ == "__main__":
    main()