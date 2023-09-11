from unittest.mock import mock
from project import operation
from project import get_data
import pytest


def main():
    test_operation()



def test_operation():
    values = ["Deposit", "Withdraw"]
    def side_effect(arg):
        return values[arg]

    mock.side_effect = side_effect

    mock.side_effect = ["Withdraw"]
    mock()


"""
def test_get_data()
    assert
"""



if __name__ == "__main__":
    main()