from select import select
from application import app,db
from application.models import *
from application.forms import *
from application.kruskals_graph import *
from flask import url_for, request, redirect, render_template

# Home
@app.route('/')
def home():
    return render_template('layout.html')


#C - driver
@app.route('/add_driver' , methods = ['GET', 'POST'])
def add_driver():
    form = DriverForm()
    if request.method == 'POST':
        driver_name = form.driver_name.data
        add_driver = Drivers(driver_name = driver_name)
        db.session.add(add_driver)
        db.session.commit()
        return redirect(url_for('drivers'))
    return render_template('add_driver.html', form = form)

#R - Drivers
@app.route('/drivers')
def drivers():
    drivers = Drivers.query.all()
    return render_template('drivers.html', drivers = drivers)

#D - Drivers
@app.route('/delete_driver/<int:driver_id>')
def delete_driver(driver_id):
    driver = Drivers.query.get(driver_id)
    for delivery in driver.driver_delivery:
        for package in delivery.delivery_packages:
            db.session.delete(package)
        db.session.delete(delivery)
    db.session.delete(driver)
    db.session.commit()
    return redirect(url_for('drivers'))


#C - Delivery
@app.route('/add_delivery' , methods = ['GET', 'POST'])
def add_delivery():
    form = DeliveryForm()
    drivers = Drivers.query.all()
    for driver in drivers:
        form.driver_id.choices.append((driver.driver_id, f'{driver.driver_name}'))
    if request.method == 'POST':
        delivery_date = form.delivery_date.data
        driver_id = form.driver_id.data
        add_delivery = Delivery(delivery_date = delivery_date, driver_id = driver_id)
        db.session.add(add_delivery)
        db.session.commit()
        return redirect(url_for('delivery'))
    return render_template('add_deliverys.html', form = form)


#R - delivery
@app.route('/delivery')
def delivery():
    deliverys = Delivery.query.all()
    return render_template('delivery.html', deliverys = deliverys)


#D - delivery
@app.route('/delete_delivery/<int:delivery_id>')
def delete_delivery(delivery_id):
    delivery = Delivery.query.get(delivery_id)
    for package in delivery.delivery_packages:
        db.session.delete(package)
    db.session.delete(delivery)
    db.session.commit()
    return redirect(url_for('delivery'))

#C - packages
@app.route('/add_package' , methods = ['GET', 'POST'])
def add_package():
    form = PackageForm()
    deliverys = Delivery.query.all()
    for delivery in deliverys:
        form.delivery_id.choices.append((delivery.delivery_id, f'{delivery.delivery_id}'))
    if request.method == 'POST':
        address = form.address.data
        status = form.status.data
        delivery_id = form.delivery_id.data
        add_package = Packages(address = address,  status = status, delivery_id = delivery_id )
        db.session.add(add_package)
        db.session.commit()
        return redirect(url_for('delivery'))
    return render_template('add_package.html', form = form)

#R - packages
@app.route('/packages/<int:delivery_id>')
def packages_specific(delivery_id):
    packages = Packages.query.filter_by(delivery_id = delivery_id)
    return render_template('packages.html', packages = packages)


#D - packages
@app.route('/delete_package/<int:package_id>')
def delete_package(package_id):
    package = Packages.query.get(package_id)
    db.session.delete(package)
    db.session.commit()
    return redirect(url_for('delivery'))

#Routes for routing
@app.route('/routing', methods = ['GET', 'POST'])
def routes():
    form = RoutingForm()
    deliverys = Delivery.query.all()
    for delivery in deliverys:
        form.delivery_id.choices.append((delivery.delivery_id, f'{delivery.delivery_id}'))
    if request.method == 'POST':
        selection = form.delivery_id.data
        return redirect(url_for('route_specific', delivery_id = selection))
    return render_template('choose_routes.html', form = form, deliverys = deliverys )

@app.route('/routing/<int:delivery_id>')
def route_specific(delivery_id):
    packages = Packages.query.filter_by(delivery_id = delivery_id)
    addresses = []
    for package in packages:
        if package.status == False:
            addresses.append(package.address)
    best_routes = WeightedGraph(addresses)
    mst = best_routes.kruskals()
    edges = mst.edges
    a_edges = []
    for edge in edges:
        a_edges.append((best_routes.addresses[edge[0]],best_routes.addresses[edge[1]], edge[2]))

    return render_template('routes.html', addresses = a_edges)
