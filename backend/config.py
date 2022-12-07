"""Config module"""

from os import environ, path

basedir = path.abspath(path.dirname(__file__))


class Config:
    """Base config"""

    SECRET_KEY = environ.get("SECRET_KEY")
    TESTING = False
    DATABASE = "sqlite:///" + path.join(basedir, "db.sqlite")
    SQLALCHEMY_DATABASE_URI = DATABASE


class TestConfig(Config):
    """Testing config"""

    DEBUG = True
    TESTING = True
    DATABASE = "sqlite:///" + path.join(basedir, "test_db.sqlite")
    SQLALCHEMY_DATABASE_URI = DATABASE
