"""App factory"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()


def create_app(testing=False):
    """Initialize flask app"""

    app = Flask(__name__, instance_relative_config=False)
    CORS(app, origins="*")

    if testing is False:
        app.config.from_object("config.Config")
    else:
        app.config.from_object("config.TestConfig")

    with app.app_context():
    
        db.init_app(app)

        from .routes import stock

        app.register_blueprint(stock.stock_bp)

    return app
