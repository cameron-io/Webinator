import os
from app import app

db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')

if (os.getenv('SQLITE') == 'true'):
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}.sqlite3'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
