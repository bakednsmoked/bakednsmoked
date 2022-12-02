"""Database modles"""

from uuid import uuid4
from sqlalchemy import Column, Integer, String

from . import Base


class Cookie(Base):
    """Cookie database object"""

    __tablename__ = "cookies"
    id = Column(String, primary_key=True, default=uuid4())
    title = Column(String, unique=True)
    amount_in_stock = Column(Integer)


def __init__(self, cookie_id=None, title=None, amount_in_stock=None):
    self.id = cookie_id
    self.title = title
    self.amount_in_stock = amount_in_stock
