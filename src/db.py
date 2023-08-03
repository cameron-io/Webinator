import os

db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')

def db_init(app):
    db_uri = f'sqlite:///{db_name}.sqlite3'\
                if os.getenv('SQLITE') == 'true'\
        else f'postgresql://{db_user}:{db_pass}@{db_host}/{db_name}'

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
