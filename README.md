#Flask Image Upload Admin Panel

This Flask project is an admin panel for uploading images to a database. Follow the instructions below to easily set it up for personal use:
Prerequisites

Before getting started, ensure that you have the following installed on your computer:

        Python 3
        pip3
        MySQLdb

Installation

    Clone the repository to your local machine:

    bash
    
    git clone https://github.com/your-username/flask-image-upload-admin-panel.git

Navigate to the project directory:

arduino

cd flask-image-upload-admin-panel

Create a .env file and paste the contents from the env.data file. Add your own credentials to the first two lines of the .env file.

Create a virtual environment in the PyEnd/ directory:

python3 -m venv venv

Activate the virtual environment:

bash

source venv/bin/activate

Install the project dependencies:

    pip3 install -r requirements.txt

Database Setup

    Ensure that your MySQL database is running.

    Open the database.sql file and copy each line.

    Paste the copied lines into your MySQL database to create the necessary tables.

Running the Project

To run the Flask project, execute the following command within the PyEnd/ folder:

arduino

flask run

This command will start the Flask development server, and the admin panel will be accessible at http://localhost:5000.

Please make sure that the MySQL database is running before starting the project.
Contributing

Contributions to the Flask Image Upload Admin Panel are welcome! If you encounter any issues or have suggestions for improvements, please feel free to create an issue or submit a pull request.
