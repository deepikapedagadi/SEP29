import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "user-secret-key")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "postgresql://postgres:welcome@localhost:5432/testdb"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
