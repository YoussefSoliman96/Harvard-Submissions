from plates import is_valid

def main():
    test_valid()

def test_valid():
    assert is_valid("HELLO") == True
    assert is_valid("hello") == True
    assert is_valid("CS50") == True
    assert is_valid("CS50P2") == False
    assert is_valid("HELLO, world") == False
    assert is_valid("50CS") == False
    assert is_valid("HELLOOOO") == False
    assert is_valid("CS05") == False
    assert is_valid("22") == False
    assert is_valid("CS.50") == False
if __name__ == "__main__":
    main()