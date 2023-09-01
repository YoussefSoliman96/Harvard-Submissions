from bank import value

def main():
    test_value()

def test_value():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("Hello, you") == 0
    assert value("hey, you") == 20
    assert value("not h") == 100
    assert value(" ") == 100








if __name__ == "__main__":
    main()