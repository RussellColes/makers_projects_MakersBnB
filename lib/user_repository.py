from lib.user import *

class UserRepository:

    def __init__(self, connection):
        self._connection = connection


    def all(self):
        records = self._connection.execute('SELECT * FROM users')
        users = []
        for record in records:
            user = User(record["id"], record["name"], record["email"], record["password"])
            users.append(user)
        return users
    
    def add(self, user):
        self._connection.execute('INSERT INTO users (name, email, password) VALUES (%s,%s,%s)', [user.name, user.email, user.password])

    def get(self, id):
        records = self._connection.execute('SELECT * FROM users WHERE id = %s', [id])
        record = records [0]
        return User(record["id"], record["name"], record["email"], record["password"])

    
