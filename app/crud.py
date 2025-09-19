from sqlmodel import Session, select
from .models import User, Book


def create_user(session: Session, user: User):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_users(session: Session):
    return session.exec(select(User)).all()


def create_book(session: Session, book: Book):
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

def get_books(session: Session):
    return session.exec(select(Book)).all()
