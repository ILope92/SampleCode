from backend.config import POSTGRES_DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class PostgreSQL:
    def __init__(self):
        self._engine = create_engine(POSTGRES_DATABASE_URL)
        self._session = sessionmaker(self._engine, expire_on_commit=False)

    @property
    def engine(self):
        return self._engine

    @property
    def session(self):
        return self._session

    @property
    def close_db(self):
        self._engine.dispose()
