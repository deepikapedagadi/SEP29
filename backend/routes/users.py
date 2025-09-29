from flask import Blueprint, jsonify
from flask.views import MethodView
from models.user import User

users_bp = Blueprint("users", __name__)

class UsersAPI(MethodView):
    def get(self):
        users = User.query.all()
        return jsonify([{"id": u.id, "email": u.email, "name": u.name} for u in users])

users_bp.add_url_rule("/users", view_func=UsersAPI.as_view("users_api"))
