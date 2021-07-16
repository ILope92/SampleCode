from datetime import date

from backend.database.init import PostgreSQL
from backend.database.models.documents import Documents
from sqlalchemy import desc, literal
from sqlalchemy.future import select
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import and_, insert, update


class CRUD_DOC:
    @classmethod
    async def open_session(cls, session):
        if session is None:
            session = PostgreSQL().session()
        return session

    @classmethod
    async def add_many(cls, models_db: tuple):
        session = PostgreSQL().session()
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
        session = await cls.open_session(session)
        query = session.query(Documents).where(model.text == Documents.text).first()
        return query

    @classmethod
    async def find_in_text(cls, text: str, session: Session = None):
        session = await cls.open_session(session)
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
        session = await cls.open_session(session)
        try:
            document = session.query(Documents).where(id == Documents.id).first()
            session.delete(document)
            session.commit()
            return document
        except Exception as e:
            session.rollback()
        finally:
            session.close()
