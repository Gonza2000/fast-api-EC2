from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
