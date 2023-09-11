from unittest.mock import Mock
from project import operation
from project import get_data
import pytest


def main():
    test_operation()



def test_operation():
    def side_effect(arg):
        return values[arg]

    mock.side_effect = side_effect
    mock('a'), mock('b'), mock('c')
    (1, 2, 3)
    mock.side_effect = [5, 4, 3, 2, 1]
    mock(), mock(), mock()
    (5, 4, 3)

"""
def test_get_data()
    assert
"""



if __name__ == "__main__":
    main()