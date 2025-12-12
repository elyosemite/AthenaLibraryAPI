import sqlalchemy as sa
from sqlalchemy import Table, Column, Integer, String

from .database import metadata

book_table = Table(
    "book",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String, nullable=False, unique=True),
    Column("description", String, nullable=False)
)
