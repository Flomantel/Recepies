from app.extensions.database import db, CRUDMixin

class Work(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    employed= db.Column(db.String(40))