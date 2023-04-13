from app.extensions.database import db, CRUDMixin

class Category(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(120))

class Recipe(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db. Column(db.String(120))
    content = db.Column(db.String(10000))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
