from flask import Flask
from flask import Flask, render_template
from flask_assets import Environment, Bundle
from dotenv import load_dotenv
import os
from flask_wtf.csrf import CSRFProtect
# init SQLAlchemy so we can use it later in our models

def create_app():
    
    app = Flask(__name__, template_folder='templates')
    
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
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
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
