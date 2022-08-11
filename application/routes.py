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
#    for delivery in driver.delivery:
 #       for item in delivery.items:
 #           db.session.delete(item)
#        db.session.delete(delivery)
    db.session.delete(driver)
    db.session.commit()
    return redirect(url_for('drivers'))


#C - Delivery
@app.route('/add_delivery' , methods = ['GET', 'POST'])
def add_delivery():
    form = DeliveryForm()
    drivers = Driver.query.all()
    for driver in drivers:
        form.driver_id.choices.append((driver.driver_id, f'{driver.driver_name}'))
    if form.validate_on_submit():
        delivery_date = form.delivery_date.data
        driver_id = form.driver_id.data
        add_delivery = Delivery(delivery_date = delivery_date, driver_id = driver_id)
        db.session.add(add_delivery)
        db.session.commit()
        return redirect(url_for('deliverys'))
    return render_template('add_deliverys.html', form = form)


#R - delivery
@app.route('/delivery')
def delivery():
    delivery = Delivery.query.all()
    return render_template('delivery.html', delivery = delivery)


#U - delivery
#@app.route('/update_delivery/<int:delivery_id>' , methods = ['GET', 'POST'])
#def update_delivery(delivery_id):
#    delivery = delivery.query.get(delivery_id)
 #   form = deliveryForm()
 #   users = User.query.all()
 #   for user in users:
#        form.driver_id.choices.append((user.driver_id, f'{user.user_name}'))
 #   if form.validate_on_submit():
  #      delivery_name = form.delivery_name.data
   #     max_delivery = form.max_delivery.data
    #    driver_id = form.driver_id.data
     #   delivery.delivery_name = delivery_name
      #  delivery.max_delivery = max_delivery
       # delivery.driver_id = driver_id
#        db.session.commit()
 #       return redirect(url_for('delivery'))
 #   form.delivery_name.data = delivery.delivery_name
 #   form.max_delivery.data = delivery.max_delivery
 #   return render_template('add_delivery.html', form = form)

#D - delivery
@app.route('/delete_delivery/<int:delivery_id>')
def delete_delivery(delivery_id):
    delivery = Delivery.query.get(delivery_id)
 #   for item in delivery.items:
 #       db.session.delete(item)
    db.session.delete(delivery)
    db.session.commit()
    return redirect(url_for('delivery'))

