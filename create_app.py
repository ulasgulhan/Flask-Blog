from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from os import path

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from post import post_bp

    app.register_blueprint(post_bp, url_prefix="/posts")

    from models.model_post import Post

    return app


app = create_app()

with app.app_context():
    db.create_all()


