from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import login_required, current_user
from .models import Patient 
from . import db

create_blueprint = Blueprint('create', __name__)

@create_blueprint.route('/create',methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        print("Posted")
        if request.form.get("submitPatient"):
            patientFirstName = request.form.get('patientFirstName')
            patientLastName = request.form.get('patientLastName')
            patientGender = request.form.get('patientGender')
            patientNotes = request.form.get('patientNotes')

            print("Got Patient")

            if len(patientFirstName) < 2:
                flash('Name needs to be longer than 1', category = 'error')
            elif len(patientLastName) < 1:
                flash('Last name needs to be longer than 1', category = 'error')
            elif len(patientGender) <1:
                flash('Please enter a gender or put n/a', category= 'error')
            else:
                new_patient = Patient(
                    patientFirstName = patientFirstName,
                    patientLastName = patientLastName,
                    gender = patientGender,
                    patientNotes = patientNotes,
                    user_id = current_user.id
                )
                #db.session.add(new_patient)
                #db.session.commit()
                #flash('Patient added', category='success')
                session["firstName"] = new_patient.patientFirstName
                session["lastName"] = new_patient.patientLastName
                session["gender"] = new_patient.gender
                if patientNotes !='':
                    session["notes"] = new_patient.patientNotes
                else:
                    session["notes"] = 'None'
                session["user_id"] = current_user.id
                return redirect(url_for('imagePrediction.imagePrediction'))
                


    return render_template("create.html",user=current_user)