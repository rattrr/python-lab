from sqlalchemy import Column, Integer, String, NUMERIC
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Test(Base):
  __tablename__ = 'test'
  id = Column(Integer, primary_key = True)
  name = Column(String(100))
  value = Column(NUMERIC)

engine = create_engine('sqlite:///example.db', echo = True)
Session = sessionmaker(bind=engine)
session = Session()

new_test = Test (
    id=3,
    name=u'ORM',
    value=0.7
)

session.add(new_test)

for test in session.query(Test).all():
    print test.id, test.name, test.value
