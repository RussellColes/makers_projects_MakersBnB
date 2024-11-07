from lib.booking_repository import *
from lib.booking import *

def test_get_all_bookings(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/users_and_spaces.sql") # Seed our database with some test data
    repository = BookingRepository(db_connection) # Create a new BookingRepository
    bookings = repository.all() # Get all bookings
    # Assert on the results
    assert bookings == [
        Booking(1, '2024-11-10', '2024-11-13', 'confirmed', 30, 1, 3),
        Booking(2, '2024-11-14', '2024-11-18', 'confirmed', 80, 2, 4),
        Booking(3, '2024-11-15', '2024-11-16', 'pending', 60, 3, 2)
    ]
    
def test_get_single_booking(db_connection):
    db_connection.seed("seeds/users_and_spaces.sql")
    repository = BookingRepository(db_connection)
    booking = repository.find(3)
    assert booking == Booking(3, '2024-11-15', '2024-11-16', 'pending', 60, 3, 2)



def test_create_booking(db_connection):
    db_connection.seed("seeds/users_and_spaces.sql")
    repository = BookingRepository(db_connection)
    repository.create(Booking(None, '2024-11-13', '2024-11-14', 'pending', 99, 2, 1))
    result = repository.all()
    assert result == [
        Booking(1, '2024-11-10', '2024-11-13', 'confirmed', 30, 1, 3),
        Booking(2, '2024-11-14', '2024-11-18', 'confirmed', 80, 2, 4),
        Booking(3, '2024-11-15', '2024-11-16', 'pending', 60, 3, 2),
        Booking(4, '2024-11-13', '2024-11-14', 'pending', 99, 2, 1)
    ]

    
def test_delete_deletes_booking(db_connection):
    db_connection.seed("seeds/users_and_spaces.sql")
    repository = BookingRepository(db_connection)
    repository.delete(3)
    result = repository.all()
    assert result == [
        Booking(1, '2024-11-10', '2024-11-13', 'confirmed', 30, 1, 3),
        Booking(2, '2024-11-14', '2024-11-18', 'confirmed', 80, 2, 4),
    ]

def test_get_booking_linked_to_id(db_connection):
    db_connection.seed("seeds/users_and_spaces.sql")
    repository = BookingRepository(db_connection)
    bens_bookings = repository.find_spaces_linked_to_id(1)
    assert bens_bookings == [
        Booking(1, '2024-11-10', '2024-11-13', 'confirmed', 30, 1, 1),
        Booking(3, '2024-11-15', '2024-11-16', 'pending', 60, 3, 1)
    ]