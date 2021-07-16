from fastapi import APIRouter

from backend.api.controllers import documents

api_router = APIRouter()

api_router.include_router(documents.router, prefix="/documents", tags=["documents"])
