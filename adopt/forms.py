from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
"""Form for adding new pets"""
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[("bunny", "Bunny"), #takes tuples, 1st is name, second is what the form shows to user. 
    ("cat", "Cat"),
    ("chicken", "Chicken"),
    ("dog", "Dog"),
    ("porcupine", "Porcupine")
    ])
    photo_url = StringField("photo url", validators=[Optional(), URL()])
    age = IntegerField("age", validators=[Optional(), NumberRange(min=0, max=100)]) #sets a minimum and maximum age range
    notes = TextAreaField("notes", validators=[Optional(), Length(min=1)]) #This field represents an HTML <textarea> and can be used to take multi-line input.

class EditPetForm(FlaskForm):
"""Allows editing of an existing pet by using this form"""

    photo_url = StringField("photo url", validators=[Optional(), URL()])
    notes = TextAreaField("notes", validators=[Optional(), Length(min=1)])
    available = BooleanField("Available?")