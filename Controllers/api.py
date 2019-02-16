from flask import Flask
from flask import json
from os import path
from flask import json

app = Flask(__name__)

from . import db
	db.init_app(app)


## The question for this application is were to just use some simple files, because it do just fine, versus the massive overhead of database.
## typiclaly there is no default wwwwroot, so those files can just lay in the same root folder as controllers lay in.
# -. Lets see what I can find out about serving a whole directory as wwwroot instead single files.
# - Lets get a angular front end instance going.
# -. What am I going to use for user and top list scoring, lets see how dificault it would be to use database of in memory one for simplisity
# otherwise we should just restore to a simple file.
# -. Check everything now compiles and sort out issues.
#http://flask.pocoo.org/docs/1.0/tutorial/database/?highlight=database
# -. change the respsonse to JSON.
# -. Set the user login settion for coockie as per tutorial



def insert(table, fields=(), values=()):
    # g.db is the database connection
    cur = g.db.cursor()
    query = 'INSERT INTO %s (%s) VALUES (%s)' % (
        table,
        ', '.join(fields),
        ', '.join(['?'] * len(values))
    )
    cur.execute(query, values)
    g.db.commit()
    id = cur.lastrowid
    cur.close()
    return id


@app.route('/User', methods=['POST'])
def user_register():

	## we could make this a json body instead, then all communication is json,
	## which would work better for the backend api and somone trying to use it.

	username = request.form.get('username')
	passport = request.form.get('password')
	surname = request.form.get('surname')
	name = request.form.get('name')

	##Check that we have vaules for all form values first and then
	## Then check that the database doesn't have the vaule inside it either.

	if not username



	insert()
	## Lets look into how to insert a record into the database.

	return jsonify(username=g.user.username,
                   email=g.user.email,
                   id=g.user.id)
    return 'Register a new user, using a post request'

@app.route('/User/<int:user_id>', methods=['PUT'])
def user_update():
    return 'update a user using a put'

@app.route('/User/<int:user_id>', methods=['DELETE'])
def user_delete():
    return 'Remove and existsing user'



@app.route('/user/login/<int:user_id>', methods=['POST'])
def user_login():
    return 'Allow the user to login and generate a sessions cookie'


@app.route('/user/lgout/<int:user_id>', methods=['POST'])
def user_logout():
    return 'Terminate the session cookie, all games'


@app.route('/game/new', methods=['POST'])
def game_new():
    return 'Create a new instance of a game, and initialize the work in session variable and completed charaters and number of tries left, only only game per user at a time supported, no instance of a game for users'

@app.route('/game/guess', methods=['POST'])
def game_guess():
    return 'basically the additional charater that is being guess, return respsonse status=ok, game-over, try=again, with auxilary fields, update complete word and remaning number of tries left.'
## If the game ends, then basically need to log a new high score.    


## ok we have to figure out how to server the full frontend from a static server.
##url_for('static', filename='style.css')
## Create a generic path handler for the frontend.
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend", "hangman-frontend")

@app.route('/<path:path>', methods=['GET'])
def static_proxy(path):
    return send_from_directory(root, path)


@app.route('/', methods=['GET'])
def redirect_to_index():
    return send_from_directory(root, 'index.html')