from flask import Flask
from flask import Flask, render_template
from flask_assets import Environment, Bundle
from dotenv import load_dotenv
import os
from flask_wtf.csrf import CSRFProtect


def create_app():
    app = Flask(__name__)
    UPLOAD_FOLDER = 'project/uploadedFiles'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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
