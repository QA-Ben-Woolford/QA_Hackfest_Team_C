
from application import db
from application.models import *


db.drop_all()
db.create_all()