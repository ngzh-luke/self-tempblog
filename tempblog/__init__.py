# root file of the app where the root config is happen here

# from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Blueprint, render_template, redirect
from decouple import config as en_var  # import the environment var
from datetime import timedelta


TIMEOUT = timedelta(hours=1)
PORT = en_var("PORT", 5500)


try:
    DOMAIN = en_var('DOMAIN_NAME')
except:
    DOMAIN = f"blog.lukecreated.com:{PORT}"


def createApp():
    app = Flask(__name__)
    # Encrepted with Environment Variable
    app.config['SECRET_KEY'] = en_var('tempblog', 'tempblogsecret')
    app.config['REMEMBER_COOKIE_SECURE'] = True
    # set session timeout (need to use with before_request() below)
    # app.config['PERMANENT_SESSION_LIFETIME'] = TIMEOUT
    app.config['TIMEZONE'] = 'Asia/Bangkok'
    app.config['SERVER_NAME'] = DOMAIN or "indev.lukecreated.com"

    from .views import views
    from .edit import edit
    app.register_blueprint(rootView, url_prefix='/')
    app.register_blueprint(views, url_prefix='/view')
    app.register_blueprint(edit, url_prefix='/edit')
    # app.register_blueprint(features, url_prefix='/')
    app.register_error_handler(404, notFound)

    return app


class About():
    version = float()
    status = str()
    build = int()
    version_note = str()

    def __init__(self, version: float = float(0.0), status: str = 'None Stated', build: int = 20221100, version_note: str = "None Stated"):
        self.version = version
        self.status = status
        self.build = build
        self.version_note = version_note

    def __str__(self) -> str:
        return str("{ " + f"Version: {self.version} | Status: {self.status} | Build: {self.build} | Updates: {self.version_note}" + " }")

    def getSystemVersion(self) -> str:
        return str(self.version)


systemInfoObject = About(version=0.3, status='Initial Development#3',
                         build=20230911, version_note='bugs fixed + add index')
systemInfo = systemInfoObject.__str__()
systemVersion = systemInfoObject.getSystemVersion()

rootView = Blueprint('rootView', __name__)


def notFound(e):
    """ not found 404 """
    return redirect("https://www.lukecreated.com/404.html")


@rootView.route('/')
def index():
    return render_template("index.html")


@rootView.route("/root-template-view/")
def root_view():
    return render_template("root.html")
