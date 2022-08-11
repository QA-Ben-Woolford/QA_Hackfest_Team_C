from application import app,db
from application.models import *
from application.forms import *
from flask import url_for, request, redirect, render_template

# Home
@app.route('/')
def home():
    return render_template('layout.html')


#C - driver
@app.route('/add_driver' , methods = ['GET', 'POST'])
def add_driver():
    form = DriverForm()
    if form.validate_on_submit():
        driver_name = form.driver_name.data
        add_driver = Drivers(driver_name = driver_name,)
        db.session.add(add_driver)
        db.session.commit()
        return redirect(url_for('drivers'))
    return render_template('add_drivers.html', form = form)
#R - Drivers
@app.route('/drivers')
def drivers():
    drivers = Drivers.query.all()
    return render_template('drivers.html', drivers = drivers)

#D - Drivers
@app.route('/delete_driver/<int:driver_id>')
def delete_driver(driver_id):
    driver = Drivers.query.get(driver_id)
#    for budget in driver.budgets:
 #       for item in budget.items:
 #           db.session.delete(item)
#        db.session.delete(budget)
    db.session.delete(driver)
    db.session.commit()
    return redirect(url_for('drivers'))