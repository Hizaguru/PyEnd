from flask import Blueprint, current_app
import os
from flask_assets import Environment, Bundle
main = Blueprint('main', __name__, template_folder='templates')

UPLOAD_FORM = "upload.html"
ALLOWED_EXTENSIONS = {'jpg', 'png'}
UPLOAD_FOLDER = 'uploadedFiles'