class Drivers(db.model):
    driver_id = db.Column(db.Integer, primary_key = True)
    driver_name = db.Column(db.string(50), nullable = False)
    driver_delivery = db.relationship('Delivery', backref = 'Drivers')

class Delivery(db.model):
    delivery_id = db.Column(db.Integer, primary_key = True)
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.driver_id'))
    delivery_date = db.Column(db.DateTime, nullable = False)
    delivery_packages = db.relationship('Packages', backref = 'Delivery')

class Packages(db.model):
    order_id = db.Column(db.Integer, primary_key = True)
    address = db.Column(db.string(50), nullable = False)
    staus = db.Column(db.Boolean, ) #How to do boolean?

#tgsrtgg