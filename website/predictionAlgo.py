from flask import Blueprint, render_template, request, flash, session, current_app, abort, send_from_directory, redirect, url_for
from tensorflow.keras.models import load_model
import cv2
import os
import numpy as np 

def predict():
    
    model = load_model('/home/JoshuaShunk/covidWebsite/website/static/Best_VGG16CNP.h5')
    #model = load_model('website/static/Best_VGG16CNP.h5')

    catigories = ['Covid 19 Pneumonia', 'Normal', 'Viral Pneumonia']
    filePath = session.get('filePath')
    fileName = session.get('fileName')
    path = '/home/JoshuaShunk/covidWebsite/website/static/uploads'
    #path = 'website/static/uploads/'

    imgPath2 = os.path.join(path, fileName)

    img = cv2.imread(imgPath2)
    img = cv2.resize(img,(224,224))

    img = np.reshape(img,[1,224,224,3])
    img = img/255

    pred = np.argmax(model.predict(img), axis=-1)

    predictedCondition = catigories[int(pred)]
    #print(predictedCondition)

    return predictedCondition