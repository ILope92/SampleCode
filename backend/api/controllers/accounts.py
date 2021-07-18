from backend.core.workers import EmailSends, ModifiedData
from backend.database.crud import CRUD_DOC, CRUD_USER
from backend.schemas.users import Registration
from fastapi import APIRouter, BackgroundTasks, Body, Depends, status
from fastapi.exceptions import HTTPException
from backend.api.responses_err import RESPONSES

router = APIRouter()


@router.post("/registration/", responses=RESPONSES)
async def registration(
    background_tasks: BackgroundTasks, data: Registration = Body(...)
):
    response = await CRUD_USER.add_user(data=data)
    if response is None:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Found email")
    background_tasks.add_task(EmailSends.add_email, data)
    return {"result": "ok"}


@router.get("/activate/")
async def activate_account(email: str = None):
    response = await CRUD_USER.update_activate(email=email)
    print(response)
    return {"result": "ok"}
