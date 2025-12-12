import sqlalchemy as sa
from sqlalchemy import MetaData

engine = sa.create_engine("sqlite:///data/mydb.sqlite")
metadata = MetaData()
