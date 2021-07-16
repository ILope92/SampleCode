from fastapi import FastAPI
from backend.core.workers import ModifiedData
from backend.api.routes import api_router
import asyncio
from backend.core.middlewares import exception_handlers

docs_config = {
    "docs_url": "/api/docs/",
    "redoc_url": "/api/redocs/",
    "openapi_url": "/api/docs/openapi.json",
}

app = FastAPI(exception_handlers=exception_handlers, **docs_config)
app.include_router(api_router, prefix="/api")


loop = asyncio.get_event_loop()
loop.create_task(ModifiedData.search())
