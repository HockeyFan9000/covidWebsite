from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():

    if request.method =='POST':
        if request.form.get("createButton"):
            return redirect(url_for('create.create'))
        elif request.form.get("viewButton"):
            return redirect(url_for('viewPast.viewPast'))
            #return render_template("viewPast.html",user=current_user)

    return render_template("home.html",user=current_user)


