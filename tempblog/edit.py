# edit the certain blog post

from flask import Blueprint, request, redirect, session, flash

edit = Blueprint('edit', __name__)


@edit.route('/')
def editIndex():
    session.clear()
    flash('Not yet available!',
          category='warning')
    # return redirect("https://devzone.lukecreated.com/")
    return "Content is not available"
