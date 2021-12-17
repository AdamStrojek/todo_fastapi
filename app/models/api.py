from sqlalchemy import Column, Boolean, String, Text

from app.models.base import Base


class TodoItem(Base):
    title = Column(String(255), nullable=False)
    text = Column(Text, nullable=True)
    done = Column(Boolean, default=False)
