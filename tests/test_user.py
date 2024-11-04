from lib.user import User

def test_class_init():
    test1 = User(None, "Ben Cole", "ben@example.com", "password")
    assert test1.id == None
    assert test1.name == "Ben Cole"
    assert test1.email == "ben@example.com"
    assert test1.password == "password"
