from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.utils import secure_filename

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patientFirstName = db.Column(db.String(150))
    patientLastName = db.Column(db.String(150))
    gender = db.Column(db.String(10))
    patientNotes = db.Column(db.String(100000))
    patientCondition = db.Column(db.String(300))
    patientDate = db.Column(db.DateTime(timezone=True), default=func.now())
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    patients = db.relationship('Patient')