from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

allowed_users = {"david": generate_password_hash("my-pass")}

allowed_tokens = {"token-david" : "david"}

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify_basic_password(username, password):
    if username not in allowed_users:
        return None
    
    if check_password_hash(password=password, pwhash=allowed_users[username]):
        return username

@token_auth.verify_token
def verify_token(token:str):
    try:
        decoded_jwt = jwt.decode(token, "my_secret", algorithms=["HS256"])
    except Exception as e:
        return None
    if decoded_jwt["name"] in allowed_users:
        return decoded_jwt["name"]
    return None