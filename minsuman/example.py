from conn import Base
from sqlalchemy import Column, Integer


class Click(Base):
    __tablename__ = 'example'
    id = Column(Integer, primary_key=True)
    click = Column(Integer)