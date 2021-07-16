from pydantic import Field, BaseModel
from typing import List, Optional
from datetime import datetime


class RequestFindTextSchema(BaseModel):
    text: str = Field(..., example="Слив инфо")


class FindText(BaseModel):
    id: int = Field(..., example=24)
    text: str = Field(..., example="Слив информации")
    rubrics: list = Field(..., example=["rub1", "rub2"])
    created_date: str = Field(...)


class ResponseFindTextSchema(BaseModel):
    result: List[FindText] = Field(example=[{"id": 10, "text": "text example"}])


class DeletePostSchema(BaseModel):
    id: int = Field(..., example=24)


class ErrorSchema(BaseModel):
    error: str = Field(..., example="error in id")
