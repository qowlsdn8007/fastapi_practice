from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, Session
import logging

from config import conf

logger = logging.getLogger(__name__)

Base = declarative_base()


class SQLAlchemy:
    def __init__(self, url: str):
        self._engine = create_engine(url, echo=True)
        self._session = scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )

    def create_database(self):
        Base.metadata.create_all(self._engine)

    def get_db(self):
        if self._session is None:
            raise Exception("not session")
        db_session = None
        try:
            db_session = self._session()
            yield db_session
        finally:
            db_session.close()

    @property
    def session(self):
        return self.get_db


c = conf()
""" Initialize Database """
db = SQLAlchemy(c.DB_URL)