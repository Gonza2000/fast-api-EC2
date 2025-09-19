from fastapi import FastAPI, Depends
from sqlmodel import Session
from .database import create_db_and_tables, get_session
from .models import User, Book
from . import crud

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/users/", response_model=User)
def create_user(user: User, session: Session = Depends(get_session)):
    return crud.create_user(session, user)

@app.get("/users/", response_model=list[User])
def read_users(session: Session = Depends(get_session)):
    return crud.get_users(session)

@app.post("/books/", response_model=Book)
def create_book(book: Book, session: Session = Depends(get_session)):
    return crud.create_book(session, book)

@app.get("/books/", response_model=list[Book])
def read_books(session: Session = Depends(get_session)):
    return crud.get_books(session)
