from fastapi import APIRouter

from backend.api.controllers import documents
from backend.api.controllers import accounts

api_router = APIRouter()

api_router.include_router(documents.router, prefix="/documents", tags=["documents"])
api_router.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
