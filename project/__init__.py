from flask import Flask
from flask import Flask, render_template
from flask_assets import Environment, Bundle
from dotenv import load_dotenv
import os
from flask_wtf.csrf import CSRFProtect
UPLOAD_FORM = "upload_form.html"
LOGIN_FORM = "http://localhost:5001"
UPLOAD_FOLDER = 'project/main/uploadedFiles'
ALLOWED_EXTENSIONS = {'jpg', 'png'}

# init SQLAlchemy so we can use it later in our models


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    load_dotenv()
    CSRFProtect(app)
    assets = Environment(app)
    assets.url = app.static_url_path
    scss = Bundle('index.scss', filters='pyscss', output='all.css')
    assets.config['SECRET_KEY'] = os.getenv('ASSET_SECRET')
    assets.config['PYSCSS_LOAD_PATHS'] = assets.load_path
    assets.config['PYSCSS_STATIC_URL'] = assets.url
    assets.config['PYSCSS_STATIC_ROOT'] = assets.directory
    assets.config['PYSCSS_ASSETS_URL'] = assets.url
    assets.config['PYSCSS_ASSETS_ROOT'] = assets.directory
    assets.register('scss_all', scss)

    # blueprint for auth routes in our app
    from .auth.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
