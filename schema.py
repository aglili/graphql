# schema.py
import strawberry
from typing import List
from models import Book
from database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session





@strawberry.type
class BookType:
    title: str
    author: str
    year: int

@strawberry.type
class Query:
    @strawberry.field
    def get_books(self) -> List[BookType]:
        db = get_db()
        print("here")
        books = db.query(Book).all()
        return books

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_book(self, title: str, author: str, year: int) -> BookType:
        db: Session = get_db()
        book = Book(title=title, author=author, year=year)
        db.add(book)
        db.commit()
        return book
    
    @strawberry.mutation
    def update_book(self, id: int, title: str, author: str, year: int) -> BookType:
        db = get_db()
        book = db.query(Book).filter(Book.id == id).first()
        book.title = title
        book.author = author
        book.year = year
        db.commit()
        return book
    
    @strawberry.mutation
    def delete_book(self, id: int) -> bool:
        db = get_db()
        book = db.query(Book).filter(Book.id == id).first()
        db.delete(book)
        db.commit()
        return True

def create_schema():
    return strawberry.Schema(query=Query, mutation=Mutation)
