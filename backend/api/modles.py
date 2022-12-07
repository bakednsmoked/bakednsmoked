"""Database modles"""

from uuid import uuid4

from . import db


class Cookie(db.Model):
    """Cookie database object"""

    __tablename__ = "cookies"
    id = db.Column(db.String, primary_key=True, unique=True)
    title = db.Column(db.String, unique=True)
    amount_in_stock = db.Column(db.Integer)

    def __init__(self, title, amount_in_stock, cookie_id=str(uuid4())):
        self.id = cookie_id
        self.title = title
        self.amount_in_stock = amount_in_stock
