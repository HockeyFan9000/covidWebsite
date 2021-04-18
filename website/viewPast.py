from flask import Blueprint, render_template, request,flash
from flask_login import login_required, current_user
from .models import Patient
import json
from . import db
from flask.json import jsonify

past_blueprint = Blueprint('viewPast', __name__)

@past_blueprint.route('/viewPast',methods=['GET', 'POST'])
@login_required
def viewPast():
    #print(Patient.patientCondition)
    if request.method == 'POST': 
        if request.form.get("patientSearch"):
            patientName = request.form.get('patientSearch')
            
    return render_template("viewPast.html",user=current_user)

@past_blueprint.route('/delete-patient', methods=['POST'])
def delete_patient():
    patient = json.loads(request.data)
    patientId = patient['patientID']
    patient = Patient.query.get(patientId)
    if patient:
        if patient.user_id == current_user.id:
            db.session.delete(patient)
            db.session.commit()
            flash(f'Patient deleted', category="success")
        else:
            flash(f'Patient: {Patient.patientFirstName} not deleted', category="error")
    else:
        flash(f'Patient: {Patient.patientFirstName} not deleted', category="error")

    return jsonify({})