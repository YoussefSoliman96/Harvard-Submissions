from fuel import convert
from fuel import gauge

def main():
    test_convert()

def test_convert():
    assert convert("1/2") == 1/2
    assert convert("2/1") == 







if __name__ == "__main__":
    main()