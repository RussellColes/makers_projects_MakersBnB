from lib.availability_repository import *
from lib.availability import *

def test_get_all_availabilities(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/users_and_spaces.sql") # Seed our database with some test data
    repository = AvailabilityRepository(db_connection) # Create a new BookingRepository
    availabilities = repository.all() # Get all bookings
    # Assert on the results
    assert availabilities == [
        Availability(1, 1, '2024-11-10', False),
        Availability(2, 1, '2024-11-11', False),
        Availability(3, 1, '2024-11-12', False),
        Availability(4, 1, '2024-11-13', True),
        Availability(5, 1, '2024-11-14', True),
        Availability(6, 1, '2024-11-15', True),
        Availability(7, 1, '2024-11-16', True),
        Availability(8, 1, '2024-11-17', True),
        Availability(9, 1, '2024-11-18', True),
        Availability(10, 2, '2024-11-10', True),
        Availability(11, 2, '2024-11-11', True),
        Availability(12, 2, '2024-11-12', True),
        Availability(13, 2, '2024-11-13', True),
        Availability(14, 2, '2024-11-14', False),
        Availability(15, 2, '2024-11-15', False),
        Availability(16, 2, '2024-11-16', False),
        Availability(17, 2, '2024-11-17', False),
        Availability(18, 2, '2024-11-18', True),
        Availability(19, 3, '2024-11-10', True),
        Availability(20, 3, '2024-11-11', True),
        Availability(21, 3, '2024-11-12', True),
        Availability(22, 3, '2024-11-13', True),
        Availability(23, 3, '2024-11-14', True),
        Availability(24, 3, '2024-11-15', False),
        Availability(25, 3, '2024-11-16', True),
        Availability(26, 3, '2024-11-17', True),
        Availability(27, 3, '2024-11-18', True)
    ]
    
def test_get_single_availability(db_connection):
    db_connection.seed("seeds/users_and_spaces.sql")
    repository = AvailabilityRepository(db_connection)
    availability = repository.find(3)
    assert availability == Availability(3, 1, '2024-11-12', False)



def test_create_availability(db_connection):
    db_connection.seed("seeds/users_and_spaces.sql")
    repository = AvailabilityRepository(db_connection)
    repository.create(Availability(None, 3, '2024-11-19', True))
    result = repository.all()
    assert result == [
        Availability(1, 1, '2024-11-10', False),
        Availability(2, 1, '2024-11-11', False),
        Availability(3, 1, '2024-11-12', False),
        Availability(4, 1, '2024-11-13', True),
        Availability(5, 1, '2024-11-14', True),
        Availability(6, 1, '2024-11-15', True),
        Availability(7, 1, '2024-11-16', True),
        Availability(8, 1, '2024-11-17', True),
        Availability(9, 1, '2024-11-18', True),
        Availability(10, 2, '2024-11-10', True),
        Availability(11, 2, '2024-11-11', True),
        Availability(12, 2, '2024-11-12', True),
        Availability(13, 2, '2024-11-13', True),
        Availability(14, 2, '2024-11-14', False),
        Availability(15, 2, '2024-11-15', False),
        Availability(16, 2, '2024-11-16', False),
        Availability(17, 2, '2024-11-17', False),
        Availability(18, 2, '2024-11-18', True),
        Availability(19, 3, '2024-11-10', True),
        Availability(20, 3, '2024-11-11', True),
        Availability(21, 3, '2024-11-12', True),
        Availability(22, 3, '2024-11-13', True),
        Availability(23, 3, '2024-11-14', True),
        Availability(24, 3, '2024-11-15', False),
        Availability(25, 3, '2024-11-16', True),
        Availability(26, 3, '2024-11-17', True),
        Availability(27, 3, '2024-11-18', True),
        Availability(28, 3, '2024-11-19', True)
    ]

    
def test_delete_deletes_availability(db_connection):
    db_connection.seed("seeds/users_and_spaces.sql")
    repository = AvailabilityRepository(db_connection)
    repository.delete(3)
    result = repository.all()
    assert result == [
        Availability(1, 1, '2024-11-10', False),
        Availability(2, 1, '2024-11-11', False),
        Availability(4, 1, '2024-11-13', True),
        Availability(5, 1, '2024-11-14', True),
        Availability(6, 1, '2024-11-15', True),
        Availability(7, 1, '2024-11-16', True),
        Availability(8, 1, '2024-11-17', True),
        Availability(9, 1, '2024-11-18', True),
        Availability(10, 2, '2024-11-10', True),
        Availability(11, 2, '2024-11-11', True),
        Availability(12, 2, '2024-11-12', True),
        Availability(13, 2, '2024-11-13', True),
        Availability(14, 2, '2024-11-14', False),
        Availability(15, 2, '2024-11-15', False),
        Availability(16, 2, '2024-11-16', False),
        Availability(17, 2, '2024-11-17', False),
        Availability(18, 2, '2024-11-18', True),
        Availability(19, 3, '2024-11-10', True),
        Availability(20, 3, '2024-11-11', True),
        Availability(21, 3, '2024-11-12', True),
        Availability(22, 3, '2024-11-13', True),
        Availability(23, 3, '2024-11-14', True),
        Availability(24, 3, '2024-11-15', False),
        Availability(25, 3, '2024-11-16', True),
        Availability(26, 3, '2024-11-17', True),
        Availability(27, 3, '2024-11-18', True)
    ]
