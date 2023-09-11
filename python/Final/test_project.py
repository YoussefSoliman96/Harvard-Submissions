from project import get_data
import pytest


def main():
    test_get_data()




def test_get_data(client_data):
    with pytest.raises(IndexError):
        get_data(client_data)




if __name__ == "__main__":
    main()