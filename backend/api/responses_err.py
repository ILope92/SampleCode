from fastapi.exceptions import HTTPException
from fastapi import status
from backend.schemas.documents import ErrorSchema


RESPONSES = {status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema}}
