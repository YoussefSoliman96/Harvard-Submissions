from seasons import get_date

def main():
    test_get_date()

def test_get_date():
    assert get_date("1996-07-24") == ('1996', '07', '24')
    assert get_date("1996-7-24") == None
    assert get_date("1996-07-2") == None
    assert get_date("24-07-1996") == None
    assert get_date("07-24-1996") == None





if __name__ == "__main__":
    main()