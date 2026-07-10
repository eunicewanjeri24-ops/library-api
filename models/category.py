from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True, index=True, min_length=2, max_length=50)

    books: list["Book"] = Relationship(back_populates="category")