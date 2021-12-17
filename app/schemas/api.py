from pydantic import validator

from app.schemas.base import BaseSchema


class TodoSchemaBase(BaseSchema):
    title: str
    text: str = ""
    done: bool = False


class InTodoSchema(TodoSchemaBase):
    ...


class TodoSchema(TodoSchemaBase):
    id: int


class OutTodoSchema(TodoSchema):
    ...
