from app import app, db
import flask_migrate

# scripts
@app.cli.command('db_init')
def db_init():
    """Initialize & migrate the models to the database."""
    with app.app_context():
        db.create_all()
        flask_migrate.Migrate(app, db)
