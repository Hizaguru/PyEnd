from flask import Blueprint, render_template

UPLOAD_FORM = "index.html"
main = Blueprint('main', __name__)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@main.route('/')
def index():
    return render_template(UPLOAD_FORM)


@main.route('/uploader')
def profile():
    return 'Profile'
