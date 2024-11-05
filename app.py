import os
from flask import Flask, request, render_template
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from lib.user_repository import UserRepository
from lib.user import User
from lib.database_connection import get_flask_database_connection
from lib.spaces_repository import SpaceRepository

# Create a new Flask app
app = Flask(__name__)
app.secret_key = 'supersecretkey(donttellanyoneorpirateswillGETyou)'

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return UserRepository.get(user_id)

# == Your Routes Here ==

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pwd']
        # user = UserRepository.get_from_email(email) DOESN'T WORK GRR
        if email == user.email and password == user.password:
            login_user(user)
            return render_template('user.html')
        else:
            return render_template('invalid_login.html')
    
    return render_template('login.html')

# GET /
# Returns the homepage
@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

# Returns the spaces page
@app.route('/spaces', methods=['GET'])
def get_all_spaces():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    return render_template("/spaces.html", spaces=spaces)

# Returns the individual spaces page
@app.route('/spaces/<int:id>', methods=['GET'])
def get_space(id):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = repository.find(id)
    return render_template("space/show_space.html", space=space)

# Returns the individual user page
@app.route('/user', methods=['GET'])
def get_user():
    name = request.args.get('name')
    return render_template('user.html', name=name)

# NEED TO COMPLETE:
@app.route('/add_property', methods=['GET'])
def add_property():
    return "ToDo"

# Logout
@app.route('/logout')
def logout():
    logout_user()
    return 'You have been logged out.'

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
