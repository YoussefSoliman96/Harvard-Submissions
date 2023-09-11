from project import operation
import pytest


def main():
    test_operation()




def test_operation():
    assert operation("Deposit") == input(f"How much cash do you want to Deposit? ")




if __name__ == "__main__":
    main()