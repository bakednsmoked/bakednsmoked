"""Database module"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from flask import current_app as app

db_eng = create_engine(app.config.get("DATABASE"))
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=db_eng)
)

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    """Initialize database"""

    from . import modles

    Base.metadata.create_all(bind=db_eng)


@app.teardown_appcontext
def shutdown_session(exception=None):
    """Shutdown db session"""

    db_session.remove()
