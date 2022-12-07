"""Database tests"""

from api import db
from api.modles import Cookie


def test_db_save(app):
    """Some database tests"""

    with app.app_context() as ctx:
        db.create_all()

        cook = Cookie(title="test_cookie", amount_in_stock=2)
        db.session.add(cook)
        db.session.commit()
        return None
