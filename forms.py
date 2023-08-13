from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, BooleanField, SelectField, IntegerField, RadioField
from wtforms.validators import InputRequired, Optional, URL

class AddPet(FlaskForm):

    name = StringField('Pet name', validators=[InputRequired()])
    species = SelectField('Species', choices=[('dog', 'Dog'), ('cat', 'Cat'), ('racoon', 'Racoon'), ('rabiit', 'Rabbit')])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional()])
    notes = TextAreaField('Comments', validators=[Optional()])

class EditPet(FlaskForm):

    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = TextAreaField('Comments', validators=[Optional()])
    available = BooleanField('Available?')