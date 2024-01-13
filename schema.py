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
    



class CreateTodo(ObjectType):
    todo = Field(Todo)

    class Arguments:
        title = String(required=True)
        description = String(required=True)

    def mutate(self,info,title,description):
        db = get_db()
        todo = TodoModel(title=title,description=description)
        db.add(todo)
        db.commit()
        db.refresh(todo)
        return CreateTodo(
            todo=todo
        )
    

class UpdateTodo(ObjectType):
    todo = Field(Todo)


    class Arguments:
        id = ID(required=True)
        title = String()
        description = String()

    def mutate(self,info,id,title=None,description=None):
        db = get_db()
        todo = db.query(TodoModel).filter(TodoModel.id == id).first()
        if title:
            todo.title = title
        if description:
            todo.description = description
        db.commit()
        db.refresh(todo)
        return UpdateTodo(
            todo=todo
        )
    
class DeleteTodo(ObjectType):
    todo = Field(Todo)

    class Arguments:
        id = ID(required=True)

    def mutate(self,info,id):
        db = get_db()
        todo = db.query(TodoModel).filter(TodoModel.id == id).first()
        if not todo:
            raise Exception("Todo not found")
        db.delete(todo)
        db.commit()
        return DeleteTodo(
            success= f"Todo with id {id} deleted successfully"
        )
