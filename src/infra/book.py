import sqlalchemy as sa
from sqlalchemy import Table, Column, Integer, String

from .database import metadata

book_table = Table(
    "book",
    metadata,
    Column("id", String, primary_key=True, unique=True),
    Column("title", String, nullable=False, unique=True),
    Column("description", String, nullable=False)
)
