from sqlalchemy import Integer, Table, Column, String

from .database import metadata

book_author_table = Table(
    "book_author",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("book_id", String, nullable=False),
    Column("author_id", String, nullable=False)
)
