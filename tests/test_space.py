from lib.space import Space

'''
When I construct a space
with the fields, id, title, location, description, price_per_night, user_id
They are reflected in the instance properties
'''

def test_constructs_with_fields():
    space = Space(1, "Title 1", "Location 1", "This is a description", 100, 1)
    assert space.id == 1
    assert space.title == "Title 1"
    assert space.location == "Location 1"
    assert space.description == "This is a description"
    assert space.price_per_night == 100
    assert space.user_id == 1