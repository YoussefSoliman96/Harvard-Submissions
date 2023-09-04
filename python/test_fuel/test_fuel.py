from fuel import convert
from fuel import gauge

def main():
    test_convert()

def test_convert():
    assert convert("1/2") == 1/2

def test_gauge():
    assert gauge("1/100") == "E"
    assert gauge("99/100") == "F"
    assert gauge("5/100") == "%5"






if __name__ == "__main__":
    main()