"""Config for pytest"""

import pytest
from api import create_app, db


@pytest.fixture
def app():
    """App context"""

    app = create_app(testing=True)
    app.test_request_context()
    db.init_app(app)

    yield app
    with app.app_context():
        db.drop_all()
        app.do_teardown_appcontext()


@pytest.fixture
def client(app):
    """Test client"""

    return app.test_client()
