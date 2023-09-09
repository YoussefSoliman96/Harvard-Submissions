from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    new_jar = Jar(5)
    assert new_jar.capacity == 5


def test_str():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(3)
    assert jar.size == 5

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    jar.withdraw(3)
    assert jar.size == 2
