from flask import Blueprint, render_template, request, flash, session, current_app, abort, send_from_directory, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .models import Patient 
from . import db
from os import path
import os
import imghdr
from .predictionAlgo import predict
from .savingPatient import savePatient


gloabalFilePath = '' 

image_blueprint = Blueprint('imagePrediction', __name__)

@image_blueprint.route('/imagePrediction',methods=['GET', 'POST'])
@login_required
def imagePrediction():
    
    #fileName =''
    #target = os.path.join(app_root, 'static/img/')
    
    patientFirstName = session.get("firstName")
    patientLastName = session.get("lastName")
    patientGender = session.get("gender")
    patientNotes = session.get("notes")
    #print(patientFirstName)

    if request.method == 'POST':
        if request.form.get("Upload"):
            uploaded_file = request.files['file']
            filename = secure_filename(uploaded_file.filename)
            session["fileName"] = filename
            if filename != '':
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in current_app.config['UPLOAD_EXTENSIONS'] or \
                    file_ext != validate_image(uploaded_file.stream):
                    abort(400)
                uploaded_file.save(os.path.join(current_app.config['UPLOAD_PATH'], filename))
                filePath = os.path.join('uploads/', filename)
                full_path = url_for('static', filename = filePath)
                global gloabalFilePath
                gloabalFilePath = filePath
                session['filePath'] = filePath
                session['fileName'] = filename
                #print(full_path)
                flash("Image uploaded succesfully", category='success')
                #print(predict())
                predictedValue = predict()
                session['patientConditon'] = predictedValue
                
                return render_template("imagePrediction.html",user=current_user,patientFirstName=patientFirstName,patientLastName=patientLastName, patientGender = patientGender, predictedValue = predictedValue, patientNotes = patientNotes, filePath = filePath, userID = current_user.get_id())
            else:
                flash("Please upload a photo", category='error')
        if request.form.get("Save"):
            patientCondition = session.get('patientConditon')
            if patientCondition !='':
                filePath = session.get("filePath")
                new_patient = savePatient()
                db.session.add(new_patient)
                db.session.commit()
                #print(Patient.patientCondition)
                #print(Patient.patientFirstName)
                flash('Patient Added', category="success")
            #return render_template("imagePrediction.html",user=current_user,patientFirstName=patientFirstName,patientLastName=patientLastName, patientGender = patientGender, userID = current_user.get_id())
           
    return render_template("imagePrediction.html",user=current_user,patientFirstName=patientFirstName,patientLastName=patientLastName,patientNotes = patientNotes, patientGender = patientGender, userID = current_user.get_id())



def validate_image(stream):
    header = stream.read(512)
    stream.seek(0) 
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

def index():
    files = os.listdir(current_app.config['UPLOAD_PATH'])
    return render_template('imagePrediction.html', files=files)

def upload(filename):
     return send_from_directory(os.path.join(
        current_app.config['UPLOAD_FOLDER'], current_user.get_id()), filename)