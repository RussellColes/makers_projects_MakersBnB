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
    p_tag = page.locator("p")
    # We assert that it has the text "This is the homepage."
    expect(p_tag).to_have_text("Welcome to Makers BnB")


'''
When a user visits /spaces
They see a list of spaces displayed on the page
'''
def test_get_spaces(page, test_web_address, db_connection):
    db_connection.seed('seeds/users_and_spaces.sql')
    page.goto(f"http://{test_web_address}/spaces")
    spaces_items = page.locator("li")
    expect(spaces_items).to_contain_text([
        "Space: Title 1"
    ])


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