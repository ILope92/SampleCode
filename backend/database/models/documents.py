from sqlalchemy import ARRAY, VARCHAR, Column, DateTime, Integer, String
from backend.database.models.base import BaseModel


class Documents(BaseModel):
    __tablename__ = "documents"
    rubrics = Column(VARCHAR(), nullable=False)
    text = Column(VARCHAR(), nullable=False)
    created_date = Column(DateTime, nullable=True)
