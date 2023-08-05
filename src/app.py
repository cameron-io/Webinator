from utils import get_env
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
    get_env('DB_ENGINE'),\
    get_env('DB_USER'),\
    get_env('DB_PASS'),\
    get_env('DB_HOST'),\
    get_env('DB_NAME')\
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# create SQLALCHEMY object
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

# define routes
from routes import signup, login, get_all_accounts
app.add_url_rule('/accounts', methods=['GET'], view_func=get_all_accounts)
app.add_url_rule('/login', methods=['POST'], view_func=login)
app.add_url_rule('/signup', methods=['POST'], view_func=signup)

# api configuration
app.config['SECRET_KEY'] = get_env('API_KEY')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
