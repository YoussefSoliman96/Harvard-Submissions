from project import Client

def main():
def test_init():
    client = Client()
    assert client.balance == 500
    new_client = Client(200)
    assert new_client.balance == 200


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(3)
    assert jar.size == 5

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.withdraw(3)
    assert jar.size == 2



if __name__ == "__main__":
    main()