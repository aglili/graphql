from sqlalchemy import Integer,Column,String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Todo(Base):
    __tablename__ = 'todo'
    id = Column(Integer,primary_key=True)
    title = Column(String(50))
    description = Column(String(100))
    