from sqlalchemy import Table, Column, Integer, String

from .database import metadata

author_table = Table(
    "author",
    metadata,
    Column("id", String, primary_key=True, unique=True),
    Column("name", String, nullable=False)
)
