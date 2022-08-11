from flask import Flask 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, BooleanField, IntegerField
from wtfforms.validators import DataRequired, length, ValidationError
from datetime import date, datetime

class DriverForm(FlaskForm):
    driver_name = StringField('Driver Name', validators=[DataRequired(), length (min=2, max = 50) ])
    submit = SubmitField('Enter')


class DeliveryForm(FlaskForm):
    