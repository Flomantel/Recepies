from flask import Flask, redirect, url_for, render_template, send_file
from . import shop, simple_pages
from app.extensions.database import db, migrate

def create_app():
    app = Flask(__name__)
    # app.config.from_object('app.config')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.secret_key = '16'

    register_extensions(app)
    register_blueprints(app)

    return app

def register_blueprints(app:Flask):
    app.register_blueprint(shop.routes.blueprint)
    app.register_blueprint(simple_pages.routes.blueprint)

def register_extensions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
