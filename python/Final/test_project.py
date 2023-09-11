from project import get_balance


def main():
    test_get_balance()



def test_get_balance():
    assert get_balance(500) == 500





if __name__ == "__main__":
    main()