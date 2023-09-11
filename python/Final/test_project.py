from project import get_data
import pytest


def main():
    test_get_data()




def test_get_data():
    with pytest.raises(IndexError):
        get_data({'id': '0', 'first_name': 'Harry', 'last_name': 'Potter', 'email': 'harry.potter@hogwarts.com', 'balance': '9500'})




if __name__ == "__main__":
    main()