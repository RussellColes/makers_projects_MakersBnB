class Booking:
    def __init__(self, id, start_date, end_date, status, total_price, user_id, space_id):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.total_price = total_price
        self.user_id = user_id  # this is the user id of the person booking, NOT the host
        self.space_id = space_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    
    def __repr__(self):
        return f"Booking({self.id}, {self.start_date}, {self.end_date}, {self.status}, {self.total_price}, {self.user_id}, {self.space_id},)"
    
INSERT INTO bookings (start_date, end_date, status, total_price, user_id, space_id) VALUES ('2024-11-10', '2024-11-13', 'confirmed', 30, 1, 1);
INSERT INTO bookings (start_date, end_date, status, total_price, user_id, space_id) VALUES ('2024-11-14', '2024-11-18', 'confirmed', 80, 2, 2);
INSERT INTO bookings (start_date, end_date, status, total_price, user_id, space_id) VALUES ('2024-11-15', '2024-11-16', 'pending', 60, 3, 1);