from unittest.mock import Mock
from project import options
from project import get_data
import pytest


def main():
    test_options()



def test_options():
    Options = options()
    Options.get = Mock(return_value = 1)
    assert options() == "Deposit"
"""
def test_get_data()
    assert
"""



if __name__ == "__main__":
    main()