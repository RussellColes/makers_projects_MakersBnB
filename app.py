import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.spaces_repository import SpaceRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5001/index
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

@app.route('/user', methods=['GET'])
def get_user():
    name = request.args.get('name')
    return render_template('user.html', name=name)

  
@app.route('/add_property', methods=['GET'])
def add_property():
    return "ToDo"


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
