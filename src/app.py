# flask imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_migrate

# load environment variables
from dotenv import load_dotenv
import utils

if (load_dotenv() != True):
    exit('Failed to initialize environment')

# creates Flask object
app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = utils.get_env('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = utils.get_env('API_KEY')

# create SQLALCHEMY object
db = SQLAlchemy(app)
import models

# endpoints
import controllers.account as account

# allow flask to manage scripts
@app.cli.command('migrate-tables')
def migrate_tables():
    """Initialize & migrate the models to the database."""
    with app.app_context():
        db.create_all()
        flask_migrate.Migrate(app, db)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
