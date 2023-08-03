import os
# flask imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# load environment variables
from dotenv import load_dotenv
if (load_dotenv() != True): exit('Failed to initialize environment')

# creates Flask object
app = Flask(__name__)
app.app_context().push()

# db configuration
from db import db_init
db_init(app)
# create SQLALCHEMY object
db = SQLAlchemy(app)
db.create_all()

# define routes
from routes import signup, login, get_all_users
app.add_url_rule('/users', methods=['GET'], view_func=get_all_users)
app.add_url_rule('/login', methods=['POST'], view_func=login)
app.add_url_rule('/signup', methods=['POST'], view_func=signup)

# api configuration
app.config['SECRET_KEY'] = os.getenv('API_KEY')

if __name__ == "__main__":
    # setting debug to True enables hot reload
    # and also provides a debugger shell
    # if you hit an error while running the server
    app.run(debug = True)
