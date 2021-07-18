from datetime import date

from backend.database.init import PostgreSQL
from backend.database.models.models import Documents, User
from sqlalchemy import desc, literal
from sqlalchemy.future import select
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import and_, insert, update
import datetime as dt


async def open_session(session):
    if session is None:
        session = PostgreSQL().session()
    return session


class CRUD_DOC:
    @classmethod
    async def add_many(cls, models_db: tuple, session: Session = None):
        session = await open_session(session)
        try:
            for model in models_db:
                if await cls.find_equal_text(model, session) is None:
                    session.add(model)
            session.commit()
        except Exception as e:
            session.rollback()
        finally:
            session.close()

    @classmethod
    async def find_equal_text(cls, model: Documents, session: Session = None):
        session = await open_session(session)
        query = session.query(Documents).where(model.text == Documents.text).first()
        return query

    @classmethod
    async def find_in_text(cls, text: str, session: Session = None):
        session = await open_session(session)
        try:
            query = (
                select(Documents)
                .where(Documents.text.like(f"%{text}%"))
                .limit(20)
                .order_by(desc(Documents.created_date))
                .subquery()
            )
            execute = session.query(query).all()
            response = [
                {
                    "id": data.id,
                    "text": data.text,
                    "rubrics": eval(data.rubrics),
                    "created_date": data.created_date.strftime("%Y-%m-%d %H:%M:%S"),
                }
                for data in execute
            ]
            return response
        finally:
            session.close()

    @classmethod
    async def delete_id(cls, id: int, session: Session = None):
        session = await open_session(session)
        try:
            document = session.query(Documents).where(id == Documents.id).first()
            session.delete(document)
            session.commit()
            return document
        except Exception as e:
            session.rollback()
        finally:
            session.close()


class CRUD_USER:
    @classmethod
    async def add_user(cls, data, session: Session = None):
        session = await open_session(session)
        if await cls.find_exists_email(data.email) is not None:
            return None
        try:
            data.date_birth = dt.datetime.strptime(data.date_birth, "%Y-%d-%m")
            new_user = User(
                **dict(data),
                activate=False,
                date_created=dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            )
            session.add(new_user)
            session.commit()
            return new_user
        except Exception as e:
            session.rollback()
        finally:
            session.close()

    @classmethod
    async def find_exists_email(cls, email: str, session: Session = None):
        session = await open_session(session)
        query = session.query(User).where(email == User.email).first()
        return query

    @classmethod
    async def update_activate(cls, email: str, session: Session = None):
        session = await open_session(session)
        try:
            query = (
                session.query(User)
                .filter(and_(User.email == email, User.activate == False))
                .update({"activate": True})
            )
            session.commit()
            return query.first()
        except Exception as e:
            session.rollback()
        finally:
            session.close()
