from application import db

class Drivers(db.Model):
    driver_id = db.Column(db.Integer, primary_key = True)
    driver_name = db.Column(db.String(50), nullable = False)
    driver_delivery = db.relationship('Delivery', backref = 'Drivers')
    
    def __str__(self):
        return f"{self.driver_id}, {self.driver_name}"

class Delivery(db.Model):
    delivery_id = db.Column(db.Integer, primary_key = True)
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.driver_id'))
    delivery_date = db.Column(db.DateTime, nullable = False)
    delivery_packages = db.relationship('Packages', backref = 'Delivery')
    
    def __str__(self):
        return f"{self.delivery_id}, {self.driver_id}, {self.delivery_date}"

class Packages(db.Model):
    package_id = db.Column(db.Integer, primary_key = True)
    delivery_id = db.Column(db.Integer, db.ForeignKey('delivery.delivery_id'))
    address = db.Column(db.String(50), nullable = False)
    status = db.Column(db.Boolean, nullable = False) 

    def __str__(self):
        return f"{self.package_id}, {self.delivery_id}, {self.address}, {self.status}"

