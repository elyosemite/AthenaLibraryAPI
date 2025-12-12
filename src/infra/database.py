import sqlalchemy as sa
from sqlalchemy import MetaData

engine = sa.create_engine("sqlite:///:memory", future=True)
metadata = MetaData()
