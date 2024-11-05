class Availability:
    def __init__(self, id, space_id, date, is_available):
        self.id = id
        self.space_id = space_id
        self.date = date
        self.is_available = is_available

    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    
    def __repr__(self):
        return f"Availability({self.id}, {self.space_id}, {self.date}, {self.is_available})"
    
