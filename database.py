from sqlalchemy import create_engine, Column, Integer, Numeric, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

'''SETUP'''
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Declare table model
class Notes(Base):
    __tablename__ = 'notes'

    note_id = Column(Integer, primary_key=True)
    note_string = Column(String())
    unique_quantity = Column(Integer())

# CREATE a table
Base.metadata.create_all(engine)

session.commit()

