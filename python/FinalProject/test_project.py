from project import get_id
from project import get_email
from project import get_balance



def main():
    test_get_id()
    test_get_balance()

def test_email():
    assert get_email("harry.potter@hogwarts.com") == "harry.potter@hogwarts.com"

def test_get_id():
    assert get_id(2) == 2

def test_get_balance():
    assert get_balance(500) == 500





if __name__ == "__main__":
    main()