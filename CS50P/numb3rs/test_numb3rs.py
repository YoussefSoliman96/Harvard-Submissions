from numb3rs import validate

def main():
    test_validate()

def test_validate():
    assert validate(r"1.1.1.1") == True
    assert validate(r"1.1.1") == False
    assert validate(r"1.1") == False
    assert validate(r"1") == False
    assert validate(r"512.2.3.4") == False
    assert validate(r"1.512.3.4") == False
    assert validate(r"1.2.512.4") == False
    assert validate(r"1.2.3.512") == False
    assert validate(r"255.255.255.255") == True

if __name__ == "__main__":
    main()
