from lib.booking import Booking
import datetime


class BookingRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all bookings
    def all(self):
        rows = self._connection.execute('SELECT * FROM bookings')
        bookings = []
        for row in rows:
            start_date_str = row["start_date"].strftime('%Y-%m-%d') if isinstance(row["start_date"], datetime.date) else row["start_date"]
            end_date_str = row["end_date"].strftime('%Y-%m-%d') if isinstance(row["end_date"], datetime.date) else row["end_date"]
            item = Booking(row["id"], start_date_str, end_date_str, row["status"], row["total_price"], row["space_id"], row["user_id"])
            bookings.append(item)
        return bookings
    
    
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * from bookings WHERE id = %s', [id])
        row = rows[0]
        start_date_str = row["start_date"].strftime('%Y-%m-%d') if isinstance(row["start_date"], datetime.date) else row["start_date"]
        end_date_str = row["end_date"].strftime('%Y-%m-%d') if isinstance(row["end_date"], datetime.date) else row["end_date"]
            
        return Booking(row["id"], start_date_str, end_date_str, row["status"], row["total_price"], row["space_id"], row["user_id"])
    
    def create(self, booking):
        rows = self._connection.execute(
            'INSERT INTO bookings (start_date, end_date, status, total_price, space_id, user_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id', 
            [booking.start_date, booking.end_date, booking.status, booking.total_price, booking.space_id, booking.user_id])
        row = rows[0]
        booking.id = row["id"]
        return booking

    
    def delete(self, id):
        self._connection.execute('DELETE FROM bookings WHERE id = %s', [id])
        return None
    
    def find_pending_bookings(self, user_id): 
        # note that the user id in the paramters here is the host id
        rows = self._connection.execute(
            """
            SELECT bookings.id, bookings.start_date, bookings.end_date, bookings.status,
            bookings.total_price, bookings.space_id, bookings.user_id AS guest_id,
            spaces.user_id AS host_id
            FROM bookings
            JOIN spaces ON spaces.id = bookings.space_id
            WHERE bookings.status = 'pending' AND spaces.user_id = %s""", [user_id])
        # again, this user_id is the host id!
        bookings = []
        for row in rows:
            start_date_str = row["start_date"].strftime('%Y-%m-%d') if isinstance(row["start_date"], datetime.date) else row["start_date"]
            end_date_str = row["end_date"].strftime('%Y-%m-%d') if isinstance(row["end_date"], datetime.date) else row["end_date"]
            item = Booking(row["id"], start_date_str, end_date_str, row["status"], row["total_price"], row["space_id"], row["guest_id"])
            bookings.append(item)
        return bookings
    
    def update_status(self, booking):
        self._connection.execute(
            'UPDATE bookings SET status = %s WHERE id = %s', [booking.status, booking.id])
        return None
    
    def find_spaces_linked_to_id(self, user_id):
        rows = self._connection.execute('SELECT * from bookings WHERE user_id = %s', [user_id])
        bookings = []
        for row in rows:
            start_date_str = row["start_date"].strftime('%Y-%m-%d') if isinstance(row["start_date"], datetime.date) else row["start_date"]
            
            end_date_str = row["end_date"].strftime('%Y-%m-%d') if isinstance(row["end_date"], datetime.date) else row["end_date"]
            
            item = Booking(row["id"], start_date_str, end_date_str, row["status"], row["total_price"], row["space_id"], row["user_id"])
            bookings.append(item)
        return bookings
    
    
    def find_user_linked_to_space(self, user_id):
        rows = self._connection.execute('SELECT users.name, bookings.user_id AS guest_id, spaces.user_id AS host_id, bookings.space_id,  bookings.status, spaces.title FROM bookings JOIN spaces on bookings.space_id = spaces.id JOIN users on users.id = bookings.user_id;')
        results = rows.fetchall()
        return results
