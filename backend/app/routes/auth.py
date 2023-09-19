from flask import Blueprint, jsonify, request
from app.dto.login_dto import LoginDtoSchema
from sqlalchemy import select
from app.database import db
from app.models.user import User
from werkzeug.security import check_password_hash
from werkzeug.exceptions import NotFound
import jwt

auth_pb = Blueprint("auth", __name__, url_prefix="/auth")
login_dto = LoginDtoSchema()


@auth_pb.route("/login", methods=["POST"])
def login_user():
    data = request.json
    creadentials = login_dto.load(data)
    print(creadentials.username)
    user = User.query.filter_by(username=creadentials.username).first()
    
    if not user:
        raise NotFound("User not found")

    if "username" not in data or "password" not in data:
        raise Exception("Unable to authenticate")

    if not check_password_hash(password=creadentials.password, pwhash=user.password):
        raise Exception("Invalid password")

    ecnoded_jwt = jwt.encode(
        {"sub": 1, "name": "david"}, "my_secret", algorithm="HS256")

    return jsonify({"token": ecnoded_jwt})
