from fastapi import APIRouter, Body, Depends
from backend.core.workers import ModifiedData
from backend.schemas.documents import (
    RequestFindTextSchema,
    ResponseFindTextSchema,
    DeletePostSchema,
    ErrorSchema,
)
from backend.database.crud import CRUD_DOC
from fastapi.exceptions import HTTPException
from fastapi import status
from backend.api.responses_err import RESPONSES

router = APIRouter()


@router.post("/find_post/", response_model=ResponseFindTextSchema)
async def find_post(data: RequestFindTextSchema = Body(...)):
    result = await CRUD_DOC.find_in_text(data.text)
    # print(result)
    return {"result": result}


@router.post(
    "/delete_post/",
    response_model=DeletePostSchema,
    responses=RESPONSES,
)
async def delete_post(data: DeletePostSchema = Body(...)):
    result = await CRUD_DOC.delete_id(data.id)
    if result is None:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Not found post")
    return {"id": data.id}
