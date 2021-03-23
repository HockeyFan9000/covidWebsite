from flask import Blueprint, render_template, request, flash, session, current_app, abort, send_from_directory, redirect, url_for
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .models import Patient 
from os import path
import os
import imghdr
from .predictionAlgo import predict


def savePatient():
    patientFirstName = session.get("firstName")
    #print('Patient First Name:' + patientFirstName)
    
    patientLastName = session.get("lastName")
    #print("Patient Last Name: " + patientLastName)

    patientGender = session.get("gender")
    #print("Patient Gender: " + patientGender)
    
    patientNotes = session.get("notes")
    

    patientCondition = session.get("patientConditon")
    #print('Patient Condition: ' + patientCondition)
    


    new_patient = Patient(user_id = current_user.id, patientFirstName = patientFirstName, patientLastName = patientLastName, gender = patientGender, patientNotes = patientNotes, patientCondition = patientCondition)
    return new_patient
    