# edit the certain blog post

from flask import render_template, Blueprint, request, redirect, url_for, session, abort, flash

edit = Blueprint('edit', __name__)


@edit.route('/')
def func():
    session.clear()
    flash('Please login again to access customized surprise present!',
          category='logout')
    # return redirect(url_for('auth.logIn'))
    # return redirect("https://devzone.lukecreated.com/")
    return "you are being redirected"
