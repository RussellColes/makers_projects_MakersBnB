# MakersBnB Group Project #

This project was a week long project using python to create a basic version of the AirBnB website. It was embarked upon following 7 weeks of intensive course and involved some elements we had worked with before and some elements which needed to be researched. We worked in a team of 5 during one week, often pair programming, to complete the task. There are still improvements we would like to make, but these will have to wait for a later date as we move on with the course! We succeeded in creating a basic version of the website, allowing users, to signup and login, list a property, view other properties and request to book a property. This was the largest codebase we had ever worked with and presented challenges initially in understanding the file structure and what should interact with what. Given this start, I'm very proud of what we achieved in 5 days. There are certainly extra features we would like to add, but this was an excellent first project to get started on.

# Makers Instructions for setting up the project #

# MakersBnB Python Project Seed

This repo contains the seed codebase for the MakersBnB project in Python (using 
Flask and Pytest).

Someone in your team should fork this seed repo to their GitHub account.
Everyone in the team should then clone this fork to their local machine to work on it.

> NOTE: If you encounter a `ModuleNotFound` error, deactivate and then reactivate your virtual env. If that doesn't help, please reach out to your coach.

## Setup

```shell
# Set up the virtual environment
; python -m venv makersbnb-venv

# Activate the virtual environment
; source makersbnb-venv/bin/activate 

# Install dependencies
(makersbnb-venv); pip install -r requirements.txt

# Install the virtual browser we will use for testing
(makersbnb-venv); playwright install
# If you have problems with the above, contact your coach

# Create a test and development database
(makersbnb-venv); createdb YOUR_PROJECT_NAME
(makersbnb-venv); createdb YOUR_PROJECT_NAME_TEST

# Open lib/database_connection.py and change the database names
(makersbnb-venv); open lib/database_connection.py

# Run the tests (with extra logging)
(makersbnb-venv); pytest -sv

# Run the app
(makersbnb-venv); python app.py

# Now visit http://localhost:5001/index in your browser
```