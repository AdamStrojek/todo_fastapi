import logging
from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from starlette import status

from app.dependencies.db import get_db, get_async_db
from app.schemas.api import InTodoSchema, OutTodoSchema
from app.models.api import TodoItem

router = APIRouter(prefix="/todo")
logger = logging.getLogger(__name__)


@router.post("/async", status_code=status.HTTP_201_CREATED, response_model=OutTodoSchema)
async def async_create_todo(
    payload: InTodoSchema, db: AsyncSession = Depends(get_async_db)
) -> OutTodoSchema:
    item = TodoItem(**payload.dict())
    db.add(item)
    await db.commit()
    output = OutTodoSchema.from_orm(item)
    return output


@router.post("/sync", status_code=status.HTTP_201_CREATED, response_model=OutTodoSchema)
def sync_create_todo(
    payload: InTodoSchema, db: Session = Depends(get_db)
) -> OutTodoSchema:
    item = TodoItem(**payload.dict())
    db.add(item)
    db.commit()
    output = OutTodoSchema.from_orm(item)
    return output


@router.get(
    "/async", status_code=status.HTTP_200_OK, response_model=List[OutTodoSchema]
)
async def async_list_todo(db: AsyncSession = Depends(get_async_db)) -> List[OutTodoSchema]:
    statement = select(TodoItem)
    result = await db.stream(statement)

    output = []

    async for item in result.scalars():
        output.append(OutTodoSchema.from_orm(item))

    return output


@router.get(
    "/sync", status_code=status.HTTP_200_OK, response_model=List[OutTodoSchema]
)
def sync_list_todo(db: AsyncSession = Depends(get_db)) -> List[OutTodoSchema]:
    statement = select(TodoItem)
    result = db.execute(statement)

    output = []

    for item in result.scalars():
        output.append(OutTodoSchema.from_orm(item))

    return output
