from lib.user_repository import *
from lib.user import *

def test_repository_init(db_connection): 
    db_connection.seed("seeds/users_and_spaces.sql")
    repository = UserRepository(db_connection)

def test_all(db_connection):
    db_connection.seed("seeds/users_and_spaces.sql")
    repository = UserRepository(db_connection)
    assert repository.all() == [User(1,'Ben Cole', 'ben@example.com', 'password'),
    User(2,'Reena Sewraz', 'reena@example.com', 'password!'),
    User(3, 'Max Joseph', 'maxj@example.com', 'password!23'),
    User(4, 'Bat man', 'justice@example.com', 'loveujoker')]

def test_add(db_connection):
    db_connection.seed("seeds/users_and_spaces.sql")
    repository = UserRepository(db_connection)
    user = User(None, 'Spiderman', 'webs@gmail.com', 'cheeseeee123')
    repository.add(user)
    assert repository.all() == [User(1,'Ben Cole', 'ben@example.com', 'password'),
    User(2,'Reena Sewraz', 'reena@example.com', 'password!'),
    User(3, 'Max Joseph', 'maxj@example.com', 'password!23'),
    User(4, 'Bat man', 'justice@example.com', 'loveujoker'),
    User(5, 'Spiderman', 'webs@gmail.com', 'cheeseeee123')
    ]


def test_get(db_connection):
    db_connection.seed("seeds/users_and_spaces.sql")
    repository = UserRepository(db_connection)
    assert repository.get(1) == User(1,'Ben Cole', 'ben@example.com', 'password')