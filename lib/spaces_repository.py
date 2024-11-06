from lib.space import Space


class SpaceRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all spaces
    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        spaces = []
        for row in rows:
            item = Space(row["id"], row["title"], row["location"], row["headline_description"], row["description"], row["price_per_night"], row["user_id"])
            spaces.append(item)
        return spaces
    
    
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * from spaces WHERE id = %s', [id])
        row = rows[0]
        return Space(row["id"], row["title"],
                    row["location"], row["headline_description"], row["description"], row["price_per_night"], row["user_id"])
    
    def find_price_per_night(self, id):
        rows = self._connection.execute(
            'SELECT * from spaces WHERE id = %s', [id])
        row = rows[0]
        space = Space(row["id"], row["title"],
                    row["location"], row["headline_description"], row["description"], row["price_per_night"], row["user_id"])
        return space.price_per_night
    
    def create(self, space):
        rows = self._connection.execute(
            'INSERT INTO spaces (title, location, headline_description, description, price_per_night, user_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id', 
            [space.title, space.location, space.headline_description, space.description, space.price_per_night, space.user_id])
        row = rows[0]
        space.id = row["id"]
        return space

      
    def delete(self, id):
        self._connection.execute('DELETE FROM spaces WHERE id = %s', [id])
        return None
    