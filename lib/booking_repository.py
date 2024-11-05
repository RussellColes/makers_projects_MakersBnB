from lib.booking import Booking


class BookingRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all spaces
    def all(self):
        rows = self._connection.execute('SELECT * FROM bookings')
        bookings = []
        for row in rows:
            item = Booking(row["id"], row["room_id"], row["guest_id"], row["start_date"], row["end_date"], row["status"])
            bookings.append(item)
        return bookings
    
    
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * from bookings WHERE id = %s', [id])
        row = rows[0]
        return Booking(row["id"], row["room_id"], row["guest_id"], row["start_date"], row["end_date"], row["status"])
    
    def create(self, booking):
        rows = self._connection.execute(
            'INSERT INTO bookings (room_id, guest_id, start_date, end_date, status, total_price) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id', 
            [booking.room_id, booking.guest_id, booking.start_date, booking.end_date, booking.status, booking.total_price])
        row = rows[0]
        booking.id = row["id"]
        return booking

    
    def delete(self, id):
        self._connection.execute('DELETE FROM bookings WHERE id = %s', [id])
        return None