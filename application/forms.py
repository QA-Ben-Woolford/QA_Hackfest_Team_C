from flask import Flask 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, BooleanField, IntegerField, SelectField
from wtfforms.validators import DataRequired, length, ValidationError
from datetime import date, datetime

class DriverForm(FlaskForm):
    driver_name = StringField('Driver Name', validators=[DataRequired(), length (min=2, max = 50) ])
    submit = SubmitField('Enter')


class DeliveryForm(FlaskForm):
    driver_id = SelectField('Driver', choices= [])
    delivery_date = DateField('Delivery Date', validators=[DataRequired()])
    driver_id = IntegerField(validators = [DataRequired()])


class PackageForm(FlaskForm):
    order_id = SelectField('Delivery Number', choices = [])
    address = StringField ('Deluvery Address', validators =[DataRequired(), length (min=10, max = 50)])
    status = BooleanField ('Delivery Status', validators = [DataRequired()])
    delivery_id = IntegerField('Delivery ID', validators = [DataRequired()])
