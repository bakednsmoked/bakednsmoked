"""Database modles"""

from uuid import uuid4
from sqlalchemy import Column, Integer, String

from . import Base


class Cookie(Base):
    """Cookie database object"""

    __tablename__ = "cookies"
    id = Column(String, primary_key=True)
    title = Column(String, unique=True)
    amount_in_stock = Column(Integer)

    def __init__(self, title, amount_in_stock, cookie_id=uuid4()):
        self.id = cookie_id
        self.title = title
        self.amount_in_stock = amount_in_stock
