from typing import List
from graphene import ObjectType,Field,String,Int,ID
from graphene_sqlalchemy import SQLAlchemyObjectType

from .models import Todo as TodoModel
from .database_config import get_db



class Todo(SQLAlchemyObjectType):
    class Meta:
        model = TodoModel
        interfaces = (ObjectType,)



class Query(ObjectType):
    todo = Field(Todo,id=ID())
    todos = Field(List(Todo))

    def resolve_todo(self,info,id):
        db = get_db()
        return db.query(TodoModel).filter(TodoModel.id == id).first()

    def resolve_todos(self,info):
        db = get_db()
        return db.query(TodoModel).all()
    
    

