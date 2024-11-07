from playwright.sync_api import Page, expect
from lib.database_connection import get_flask_database_connection
from lib.spaces_repository import SpaceRepository
from flask import Flask, request

'''
We can render the homepage page
'''
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/")
    # We look at the <p> tag
    text_tag = page.locator(".t-text")
    # We assert that it has the text "This is the homepage."
    expect(text_tag).to_have_text("Please fill in your details:")


'''
When a user clicks on a space
The details of the space are displayed
'''
def test_click_on_space_link(page, test_web_address, db_connection):
    db_connection.seed("seeds/users_and_spaces.sql")
    page.goto(f"http://{test_web_address}/spaces")
    page.click("text=Title 1")
    title_tag = page.locator(".t-title").nth(0)
    expect(title_tag).to_have_text("Space: Title 1")

'''
When a user visits /spaces
They see a list of spaces displayed on the page
'''
def test_get_spaces(page, test_web_address, db_connection):
    db_connection.seed('seeds/users_and_spaces.sql')
    page.goto(f"http://{test_web_address}/spaces")
    spaces_items = page.locator("h5")
    expect(spaces_items).to_contain_text([
        "Title 1"
    ])



'''
When we create a new space
We see it in the list of spaces
'''

def test_create_space(db_connection, page, test_web_address):
    db_connection.seed("seeds/users_and_spaces.sql")
    page.goto(f"http://{test_web_address}/user")

    page.click("text='List another space'")

    page.fill("input[name='title']", "Title 4")
    page.fill("input[name='location']", "Location 4")
    page.fill("input[name='headline_description']", "Headline Description 4")
    page.fill("input[name='description']", "Description 4")
    page.fill("input[name='price_per_night']", "10")
    page.fill("input[name='user_id']", "4")

    page.click("text=Submit")

    title_element = page.locator(".t-title")
    expect(title_element).to_have_text("Space: Title 4")

    location_element = page.locator(".t-location")
    expect(location_element).to_have_text("Location: Location 4")
    
    headline_description_element = page.locator(".t-headline_description")
    expect(headline_description_element).to_have_text("Headline Description: Headline Description 4")

    description_element = page.locator(".t-description")
    expect(description_element).to_have_text("Description: Description 4")

    price_element = page.locator(".t-price_per_night")
    expect(price_element).to_have_text("Price Per Night: 10")

    owner_element = page.locator(".t-user_id")
    expect(owner_element).to_have_text("Owner: 4")


'''
When a user is on the spaces page
They can access the dashboard
'''
def test_access_dashboard(db_connection, page, test_web_address):
    db_connection.seed("seeds/users_and_spaces.sql")
    page.goto(f"http://{test_web_address}/spaces")
    page.click("text='My Account'")
    page.click("text='Dashboard'")
    heading = page.locator("h3")
    expect(heading).to_have_text("Bookings")


'''
When a user logs in
and clicks on My Account and then clicks My Dashboard
They see their spaces
'''
def test_show_individual_users_spaces(db_connection, page, test_web_address):
    db_connection.seed("seeds/users_and_spaces.sql")
    page.goto(f"http://{test_web_address}/user/1")
    heading = page.locator("h3")
    expect(heading).to_have_text("Your Spaces")
    title_element = page.locator(".t-title")
    expect(title_element).to_have_text("Title 1")


'''
When a user logs in
and clicks on My Account and then clicks My Dashboard
They see their bookings
'''
def test_show_individual_users_bookings(db_connection, page, test_web_address):
    db_connection.seed("seeds/users_and_spaces.sql")
    page.goto(f"http://{test_web_address}/user/1")
    heading = page.locator("h2")
    expect(heading).to_have_text("Your Bookings")
    title_element = page.locator(".t-title")
    expect(title_element).to_have_text("Status")

def test_create_booking(db_connection, page, test_web_address):
    db_connection.seed("seeds/users_and_spaces.sql")
    page.goto(f"http://{test_web_address}/spaces/1")
    page.select_option("#start_date", "2024-11-13")
    page.select_option("#end_date", "2024-11-15")
    page.click("text='Submit'")
    text_tag = page.locator(".t-text")
    expect(text_tag).to_have_text("Your booking request has been submitted!")
