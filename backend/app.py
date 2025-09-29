#from flask import Flask
from config import Config
from extensions import db, cors
from routes.auth import auth_bp
from routes.users import users_bp
from flask import Flask, request, jsonify
#from flask_sqlalchemy import SQLAlchemy
from flask.views import MethodView
from werkzeug.security import generate_password_hash, check_password_hash
"""import jwt
import datetime
import base64 """
#import os
#import json
#from flask_cors import CORS
#app = Flask(__name__)
#CORS(app)
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    #CORS(app)
    # Init extensions
    db.init_app(app)
    cors.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/")
    app.register_blueprint(users_bp, url_prefix="/")

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=1200)
