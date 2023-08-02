import os
# flask imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
if (load_dotenv() != True): exit('Failed to initialize environment')
# creates Flask object
app = Flask(__name__)
# db configuration
import db
# create SQLALCHEMY object
db = SQLAlchemy(app)
# define routes
import routes

# api configuration
app.config['SECRET_KEY'] = os.getenv('API_KEY')

app.app_context().push()

if __name__ == "__main__":
    # setting debug to True enables hot reload
    # and also provides a debugger shell
    # if you hit an error while running the server
    app.run(debug = True)
