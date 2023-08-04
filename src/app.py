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
app.config['SQLALCHEMY_DATABASE_URI'] = '{}://{}:{}@{}/{}'.format(\
    os.getenv('DB_ENGINE'),\
    os.getenv('DB_USER'),\
    os.getenv('DB_PASS'),\
    os.getenv('DB_HOST'),\
    os.getenv('DB_NAME')\
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# create SQLALCHEMY object
db = SQLAlchemy(app)
db.create_all()

# define routes
from routes import signup, login, get_all_accounts
app.add_url_rule('/accounts', methods=['GET'], view_func=get_all_accounts)
app.add_url_rule('/login', methods=['POST'], view_func=login)
app.add_url_rule('/signup', methods=['POST'], view_func=signup)

# api configuration
app.config['SECRET_KEY'] = os.getenv('API_KEY')

if __name__ == "__main__":
    # setting debug to True enables hot reload
    # and also provides a debugger shell
    # if you hit an error while running the server
    app.run(host='0.0.0.0', debug=True)
