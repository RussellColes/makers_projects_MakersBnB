from lib.booking import Booking

'''
When I construct a booking
with the fields, room_id, guest_id, start_date, end_date, status
They are reflected in the instance properties
'''
def test_constructs_with_fields():
    booking = Booking(1, "13/12/2024", "15/12/2024", "Pending", 99,  1, 2)
    assert booking.id == 1
    assert booking.start_date == "13/12/2024"
    assert booking.end_date == "15/12/2024"
    assert booking.status == "Pending"
    assert booking.total_price == 99
    assert booking.space_id == 1
    assert booking.user_id == 2


'''
Test for Equality
'''
def test_equality_booking():
    booking_1 = Booking(1, "13/12/2024", "15/12/2024", "Pending", 99, 2, 1)
    booking_2 = Booking(1, "13/12/2024", "15/12/2024", "Pending", 99, 2, 1)
    assert booking_1 == booking_2


'''
Test for Formatting
'''
def test_formatting_booking():
    booking = Booking(1, "13/12/2024", "15/12/2024", "Pending", 99, 2, 1)
    assert str(booking) == "Booking(1, 13/12/2024, 15/12/2024, Pending, 99, 2, 1)"