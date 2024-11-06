class Booking:
    def __init__(self, id, start_date, end_date, status, total_price, space_id,  user_id):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.total_price = total_price
        self.space_id = space_id
        self.user_id = user_id


    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    
    def __repr__(self):
        return f"Booking({self.id}, {self.start_date}, {self.end_date}, {self.status}, {self.total_price}, {self.space_id}, {self.user_id})"