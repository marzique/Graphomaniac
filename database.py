from sqlalchemy import create_engine, Column, Integer, Numeric, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from helpers import *

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

test_note_string = "Really really long string, with comma and a dot."
test_note_quantity = unicounter(test_note_string)



'''ACTIONS'''

# fill in one row (add new note)
note1 = Notes(note_string = test_note_string, unique_quantity = test_note_quantity)

# put Notes instance to session
session.add(note1)
session.commit()


print(note1.unique_quantity)