"""App factory"""
import threading
from flask import Flask


def create_app(testing=False):
    """Initialize flask app"""

    app = Flask(__name__, instance_relative_config=False)

    if testing is False:
        app.config.from_object("config.Config")
    else:
        app.config.from_object("config.TestConfig")

    with app.app_context():
        from .db import init_db

        init_db()

        from .routes import stock

        app.register_blueprint(stock.stock_bp)

        from .ws import start_ws

        ws_thread = threading.Thread(target=start_ws)
        ws_thread.start()

    return app
