from flask import Blueprint, request, jsonify
from flask.views import MethodView
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models.user import User
from utils.token import generate_token
import jwt

auth_bp = Blueprint("auth", __name__)

class RegisterAPI(MethodView):
    def post(self):
        data = request.json or {}
        email = data.get("email")
        name = data.get("name")
        password = data.get("password")

        if not email or not name or not password:
            return jsonify({"message": "Email, name and password are required"}), 400

        if User.query.filter_by(email=email).first():
            return jsonify({"message": "User already exists"}), 409

        hashed = generate_password_hash(password)
        user = User(email=email, name=name, password=hashed, password_plain=password)
        db.session.add(user)
        db.session.commit()

        token = generate_token(user)
        return jsonify({"message": "User registered successfully", "token": token})

class LoginAPI(MethodView):
    def post(self):
        auth = request.headers.get("Authorization", "")
        if auth.startswith("Bearer "):
            token = auth.split(" ", 1)[1].strip()
            try:
                payload = jwt.decode(token, request.app.config["SECRET_KEY"], algorithms=["HS256"])
                return jsonify({"message": "Login via token successful", "payload": payload})
            except jwt.ExpiredSignatureError:
                return jsonify({"message": "Token expired"}), 401
            except jwt.InvalidTokenError:
                return jsonify({"message": "Invalid token"}), 401

        data = request.json or {}
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"message": "Email and password are required"}), 400

        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({"message": "Invalid credentials"}), 401

        token = generate_token(user)
        return jsonify({"message": "Login successful", "token": token})

auth_bp.add_url_rule("/register", view_func=RegisterAPI.as_view("register_api"))
auth_bp.add_url_rule("/login", view_func=LoginAPI.as_view("login_api"))
