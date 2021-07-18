from pydantic import Field, BaseModel
from typing import List, Optional
from datetime import datetime


class ActivateAccount(BaseModel):
    code: int = Field(..., example=1492)


class Registration(BaseModel):
    first_name: str = Field(..., example="ivan")
    last_name: str = Field(..., example="ivanov")
    date_birth: str = Field(..., example="1995-22-08")
    email: str = Field(..., example="test@mail.ru")
    password: str = Field(..., example="test")


class User(Registration, ActivateAccount):
    activate: bool = Field(default=False)
    date_created: str = Field(default=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
