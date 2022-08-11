from application import app,db
from application.models import *
from application.forms import *
from flask import url_for, request, redirect, render_template

# Home
@app.route('/')
def home():
    return render_template('layout.html')


#C - User
@app.route('/add_driver' , methods = ['GET', 'POST'])
def add_driver():
    form = DriverForm()
    if form.validate_on_submit():
        driver_name = form.driver_name.data
        add_driver = User(driver_name = driver_name,)
        db.session.add(add_driver)
        db.session.commit()
        return redirect(url_for('drivers'))
    return render_template('add_drivers.html', form = form)
#R - User
@app.route('/drivers')
def drivers():
    drivers = User.query.all()
    return render_template('drivers.html', drivers = drivers)

#U - User
@app.route('/update_user/<int:user_id>' , methods = ['GET', 'POST'])
def update_user(user_id):
    user = User.query.get(user_id)
    form = UserForm()
    if form.validate_on_submit():
        user_name = form.user_name.data
        email = form.email.data
        annual_salary = form.annual_salary.data
        user.user_name = user_name
        user.email = email
        user.annual_salary = annual_salary
        db.session.commit()
        return redirect(url_for('drivers'))
    form.user_name.data = user.user_name
    form.email.data = user.email
    form.annual_salary.data = user.annual_salary
    return render_template('add_drivers.html', form = form)
#D - User
@app.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    user = User.query.get(user_id)
    for budget in user.budgets:
        for item in budget.items:
            db.session.delete(item)
        db.session.delete(budget)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('drivers'))