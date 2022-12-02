"""Config module"""

from os import environ


class Config:
    """Base config"""

    SECRET_KEY = environ.get("SECRET_KEY")
    TESTING = False
    DATABASE = "sqlite:///db.sqlite"


class TestConfig(Config):
    """Testing config"""

    DEBUG = True
    TESTING = True
    DATABASE = "sqlite:///test_db.sqlite"
