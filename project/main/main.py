from flask import current_app, render_template, request, flash, redirect
import time
from werkzeug.utils import secure_filename
import os
from project.database.db import insert_image, connect_to_database, read_query, db_query
from .import main
UPLOAD_FORM = "upload.html"
ALLOWED_EXTENSIONS = {'jpg', 'png'}
UPLOAD_FOLDER = 'uploadedFiles'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def table_headings():
    headings = ("ID", "Image Name", "Caption", "Size", "")
    return headings


@main.route('/upload')
def index():
    return render_template(UPLOAD_FORM)


@main.route('/table', methods=['GET', 'POST'])
def list_images():
    connection = connect_to_database()
    select_images = "SELECT Id, Filename, Caption, Size FROM Image"
    read_query(connection, select_images)

    return render_template("table.html", headings=table_headings(), data=read_query(connection, select_images))


@main.route('/uploader', methods=['POST', 'GET'])
def profile():
    print("before if method")
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            print("no file")
            flash('No file part')
            time.sleep(2)
            return redirect('/')

        f = request.files['file']

        if f.filename == '':
            flash("No file selected", "Warning")
            time.sleep(5)
            return redirect(UPLOAD_FORM)
        elif not allowed_file(f.filename):
            flash("File not allowed")
            time.sleep(5)
            return redirect('/')

        # If allowed inserts the filename, blob, caption and size of the file into the database.
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            caption = request.form.get("caption")
            image_folder = os.path.join(
                current_app.config['UPLOAD_FOLDER'], filename)
            f.save(image_folder)
            # Calculate the size of the photo
            file = request.files['file']
            file.seek(0, os.SEEK_END)
            file_length = file.tell() / 1000
            file_length = str(file_length) + " kb"

            print(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

            insert_image(filename, image_folder, caption, file_length)
            flash("File uploaded successfully", "info")
            time.sleep(5)
            return redirect("/upload")


@main.route('/delete/<int:id>')
def delete_image(id):
    connection = connect_to_database()
    delete_image = "DELETE FROM Image where Id=" + str(id)
    print(delete_image)
    try:
        db_query(connection, delete_image)
        return redirect('/table')
    except:
        logging.exception('Error while deleting database object.')
        raise
