from sqlalchemy import Column, Integer, String, NUMERIC
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import ForeignKey

Base = declarative_base()

class Book(Base):
  __tablename__ = 'books'
  id = Column(Integer, primary_key = True)
  title = Column(String(100))
  author = Column(String(100))
  year = Column(Integer)

class Person(Base):
    __tablename__ = 'person'
    pid = Column(Integer, primary_key = True)
    name = Column(String(100))
    bookid = Column(Integer, ForeignKey("books.id"))

engine = create_engine('sqlite:///books.db', echo = True)
Session = sessionmaker(bind=engine)
session = Session()



for books in session.query(Book).all():
    print books.id, books.title
