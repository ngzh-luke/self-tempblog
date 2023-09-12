# edit the certain blog post

from flask import Blueprint, request, redirect, flash

edit = Blueprint('edit', __name__)


@edit.route('/')
def editIndex():
    flash('Not yet available!',
          category='warning')
    return " Sorry, Content is not yet available!"
