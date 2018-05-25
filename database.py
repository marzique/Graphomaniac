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


'''ACTIONS'''
# Test with 2 strings

note_string4 = "Really really long string, even longer than a previous one sdasd asd sd asd a a asd aa."
note_string1 = "Really really long string, with comma and a dot."
note_string2 = "Really really long string, even longer than a previous one."
note_string3 = "really Really reAlLy ok koko."

# fill in one row (add new note)
note1 = Notes(note_string = note_string1,
              unique_quantity = unicounter(note_string1))

note2 = Notes(note_string = note_string2,
              unique_quantity = unicounter(note_string2))

note3 = Notes(note_string = note_string3,
              unique_quantity = unicounter(note_string3))

note4 = Notes(note_string = note_string4,
              unique_quantity = unicounter(note_string4))



# put Notes instance to session
# use session.bulk_save_objects([note1, note2, noteN]) when multiple objects filling in
# session.add(note1)
session.bulk_save_objects([note1, note2, note3, note4])
session.commit()

# query to pull of data(notes) ordered by uniqueness
for note in session.query(Notes).order_by(Notes.unique_quantity):
    print(note.note_string + " : " + str(note.unique_quantity))
