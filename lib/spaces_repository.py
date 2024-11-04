from lib.space import *


class SpaceRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all books
    def all(self):
        rows = self._connection.execute('SELECT * from spaces')
        spaces = []
        for row in rows:
            item = Space(row["id"], row["location"], row["description"], row["price_per_night"], row["user_id"])
            spaces.append(item)
        return spaces