from project import Client


def test_init():
    client = Client()
    assert client.balance == 500
    new_client = Client(200)
    assert new_client.balance == 200


def test_str():
    client = Client()
    assert str(client) == ""
    jar.deposit(1)
    assert str(jar) == 1 + "🍪"

def test_deposit():
    client = Client()
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(3)
    assert jar.size == 5

def test_withdraw():
    client = Client()
    jar.deposit(5)
    assert jar.size == 5
    jar.withdraw(3)
    assert jar.size == 2

