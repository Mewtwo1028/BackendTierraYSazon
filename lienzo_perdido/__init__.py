from flask import Flask
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY='mykey',
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE')
    )

    from . import db
    from . import lienzo
    from . import auth
    app.register_blueprint(lienzo.bp)
    app.register_blueprint(auth.bp)
    db.init_app(app)
    return app