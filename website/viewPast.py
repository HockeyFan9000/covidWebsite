from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Patient

past_blueprint = Blueprint('viewPast', __name__)

@past_blueprint.route('/viewPast')
@login_required
def viewPast():
    print(Patient.patientCondition)
    return render_template("viewPast.html",user=current_user)


