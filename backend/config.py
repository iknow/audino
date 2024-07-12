import os

from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = os.environ.get("SQLALCHEMY_ECHO", "False") == "True"
    REDIS_URL = os.environ.get("JWT_REDIS_STORE_URL", "")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "")
    JWT_ACCESS_TOKEN_EXPIRES = os.environ.get(
        "JWT_ACCESS_TOKEN_EXPIRES", timedelta(days=7)
    )
    JWT_BLACKLIST_ENABLED = True
    JWT_HEADER_TYPE = None
    JWT_BLACKLIST_TOKEN_CHECKS = ["access"]
    UPLOAD_FOLDER = './uploads'
    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
    GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"
