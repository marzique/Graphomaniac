from flask import Flask, flash, redirect, render_template, request, session, url_for
from helpers import unicounter
from sqlalchemy import create_engine, Column, Integer, Numeric, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# configure application
app = Flask(__name__)

'''SETUP DATABASE'''
engine = create_engine('sqlite:///notes.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

'''Cleares table after restart'''
def clear_table():
    session.query(Notes).delete()
    session.commit()

# Declare table model
class Notes(Base):
    __tablename__ = 'notes'

    note_id = Column(Integer, primary_key=True)
    note_string = Column(String())
    unique_quantity = Column(Integer())

# CREATE a table
Base.metadata.create_all(engine)
clear_table()

@app.route("/" , methods=["GET", "POST"])
@app.route("/index.html" , methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # retrieve note from input box
        note = request.form.get("note")
        # empty string check
        if not note:
            return render_template("error.html")

        '''retreive note'''
        print(note + " : " + str(unicounter(note)))

        '''ACTIONS'''

        # fill in one row (adding new note)
        note1 = Notes(note_string=note, unique_quantity=unicounter(note))

        # put Notes instance to session
        # use session.bulk_save_objects([note1, note2, noteN]) when multiple objects filling in
        session.add(note1)
        # session.bulk_save_objects([note1, note2, note3, note4])


        # query to pull of data(notes) ordered by uniqueness
        for note in session.query(Notes).order_by(Notes.unique_quantity):
            print(note.note_string + " : " + str(note.unique_quantity))

        session.commit()

        return render_template("notes.html")

    else:
        return render_template("index.html")


@app.route("/notes.html")
def notes():
    return render_template("notes.html")

@app.route("/clear")
def clear():
    clear_table()
    return render_template("notes.html")


if __name__ == '__main__':
    app.run(debug=True)