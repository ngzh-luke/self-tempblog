# display the certain blog post that users will see when requested in certain url

from flask import render_template, Blueprint, request, redirect, url_for, session, flash

views = Blueprint('views', __name__)


@views.route('/')
def viewIndex():
    return redirect(url_for('rootView.index'))


@views.route('/1/')
def renderUPsView():
    return render_template("ups2023.html")


@views.route('/2/')
def renderASEANview():
    return render_template("asean2023.html")
    # return redirect('https://google.com')
