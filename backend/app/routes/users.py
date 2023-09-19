
from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash
from app.models.user import User, UserSchema
from app.database import db
from . import token_auth

users_bp = Blueprint("users", __name__, url_prefix="/users")
user_schema = UserSchema()


@users_bp.route("/", methods=["GET"])
@token_auth.login_required
def get_all_users():
    users = User.query.all()
    return jsonify(user_schema.dump(users, many=True))


@users_bp.route("/", methods=["POST"])
@token_auth.login_required
def create_user():
    data = request.json
    user = User()
    user.username = data["username"]
    user.email = data["email"]
    user.password = generate_password_hash(data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify(data), 201


@users_bp.route("/<user_id>", methods=["GET"])
@token_auth.login_required
def get_all_user(user_id: int):
    user = User.query.filter_by(id=user_id).one()
    return {"id": user.id, "username": user.username}
