from seasons import get_date

def main():
    test_get_date()

def test_get_date():
    assert get_date("1996-07-24") == "Fourteen million, two hundred sixty-seven thousand, five hundred twenty minutes"
    assert get_date("1996-7-24") == "Invalid format"
    assert get_date("1996-07-2") == "Invalid format"
    assert get_date("24-07-1996") == "Invalid format"
    assert get_date("07-24-1996") == "Invalid format"





if __name__ == "__main__":
    main()