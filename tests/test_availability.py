from lib.availability import Availability

'''
When I construct an availability
with the fields, room_id, date, is_available
They are reflected in the instance properties
'''
def test_availability_constructs_with_fields():
    availability = Availability(1, 2, "13/12/2024", True)
    assert availability.id == 1
    assert availability.date == "13/12/2024"
    assert availability.is_available == True

'''
Test for Equality
'''
def test_eqality_availability():
    availability_1 = Availability(1, 2, "13/12/2024", True)
    availability_2 = Availability(1, 2, "13/12/2024", True)
    assert availability_1 == availability_2


'''
Test for Formatting
'''
def test_formatting_availability():
    availability = Availability(1, 2, "13/12/2024", True)
    assert str(availability) == Availability(1, 2, "13/12/2024", True)

"""
INSERT INTO availabilities (space_id, date, is_available) VALUES (1, '2024-11-10', False);
INSERT INTO availabilities (space_id, date, is_available) VALUES (1, '2024-11-11', False);
INSERT INTO availabilities (space_id, date, is_available) VALUES (1, '2024-11-12', False);
INSERT INTO availabilities (space_id, date, is_available) VALUES (1, '2024-11-13', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (1, '2024-11-14', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (1, '2024-11-15', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (1, '2024-11-16', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (1, '2024-11-17', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (1, '2024-11-18', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (2, '2024-11-10', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (2, '2024-11-11', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (2, '2024-11-12', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (2, '2024-11-13', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (2, '2024-11-14', False);
INSERT INTO availabilities (space_id, date, is_available) VALUES (2, '2024-11-15', False);
INSERT INTO availabilities (space_id, date, is_available) VALUES (2, '2024-11-16', False);
INSERT INTO availabilities (space_id, date, is_available) VALUES (2, '2024-11-17', False);
INSERT INTO availabilities (space_id, date, is_available) VALUES (2, '2024-11-18', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (3, '2024-11-10', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (3, '2024-11-11', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (3, '2024-11-12', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (3, '2024-11-13', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (3, '2024-11-14', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (3, '2024-11-15', False);
INSERT INTO availabilities (space_id, date, is_available) VALUES (3, '2024-11-16', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (3, '2024-11-17', True);
INSERT INTO availabilities (space_id, date, is_available) VALUES (3, '2024-11-18', True);
"""