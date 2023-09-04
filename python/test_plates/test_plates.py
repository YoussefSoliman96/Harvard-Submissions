from plates import is_valid

def main():
    test_valid()

def test_validd():
    assert is_valid("HELLO") == True
    assert is_valid("hello") == True
    assert is_valid("CS50") == True
    assert is_valid("CS50P2") == False
    assert is_valid("HELLO, world") == False


    main()