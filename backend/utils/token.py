import jwt
import datetime
import base64
import json
from flask import current_app

def generate_token(user, hours=1):
    payload = {
        "user_id": user.id,
        "email": user.email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=hours)
    }
    token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")
    return token if isinstance(token, str) else token.decode("utf-8")

def _b64url_decode(data: str) -> bytes:
    if isinstance(data, str):
        data = data.encode("utf-8")
    rem = len(data) % 4
    if rem:
        data += b"=" * (4 - rem)
    return base64.urlsafe_b64decode(data)

def decode_jwt_unverified(token: str):
    parts = token.split(".")
    if len(parts) != 3:
        raise ValueError("Token must have exactly 3 parts.")
    h_b64, p_b64, s_b64 = parts
    header = json.loads(_b64url_decode(h_b64))
    payload = json.loads(_b64url_decode(p_b64))
    return header, payload, s_b64
