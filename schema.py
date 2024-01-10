from typing import List
from graphene import ObjectType,Field,String,Int,ID
from graphene_sqlalchemy import SQLAlchemyObjectType

from .models import Todo as TodoModel
from .database_config import get_db



class Todo(SQLAlchemyObjectType):
    class Meta:
        model = TodoModel
        interfaces = (ObjectType,)





