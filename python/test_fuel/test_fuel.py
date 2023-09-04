from fuel import convert
from fuel import gauge
import pytest

def main():
    test_convert()
    test_division()
    test_value()

def test_convert():
    assert convert("1/2") == 50
    assert convert("1/100") == 1
    assert convert("99/100") == 99


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(5) == "%5"


def test_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_value():
    with pytest.raises(ValueError):
        convert("d/c")

if __name__ == "__main__":
    main()