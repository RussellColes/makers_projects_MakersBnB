from lib.spaces_repository import *
from lib.space import *

def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/spaces.sql") # Seed our database with some test data
    repository = SpaceRepository(db_connection) # Create a new BookRepository

    spaces = repository.all() # Get all books

    # Assert on the results
    assert spaces == [
        Space(1, 'Title 1', 'Location 1', 'Description 1', 10, 1),
        Space(2, 'Title 2', 'Location 2', 'Description 2', 20, 2),
        Space(3, 'Title 3', 'Location 3', 'Description 3', 30, 3)
        ]