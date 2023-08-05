from app import db

# Database ORMs
class Account(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    public_id = db.Column(db.String(50), unique = True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(70), unique = True)
    password = db.Column(db.String(255))

    def __repr__(self):
        return '<User %r>' % self.username
