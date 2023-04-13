from app.extensions.database import db

class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    employed= db.Column(db.String(40))