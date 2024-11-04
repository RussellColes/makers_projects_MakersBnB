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
    
def test_get_single_space(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repository = SpaceRepository(db_connection)
    space = repository.find(3)
    assert space == Space(3, 'Title 3', 'Location 3', 'Description 3', 30, 3)



def test_create_space(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repository = SpaceRepository(db_connection)

    repository.create(Space(None, "Title 4", "Location 4", "Description 4", 40, 2))

    result = repository.all()
    assert result == [
        Space(1, 'Title 1', 'Location 1', 'Description 1', 10, 1),
        Space(2, 'Title 2', 'Location 2', 'Description 2', 20, 2),
        Space(3, 'Title 3', 'Location 3', 'Description 3', 30, 3),
        Space(4, 'Title 4', 'Location 4', 'Description 4', 40, 2)

    ]

def test_delete_deletes_record(db_connection):
    db_connection.seed("seeds/spaces.sql")

    repository = SpaceRepository(db_connection)
    repository.delete(3)

    result = repository.all()

    assert result == [
        Space(1, 'Title 1', 'Location 1', 'Description 1', 10, 1),
        Space(2, 'Title 2', 'Location 2', 'Description 2', 20, 2)
    ]