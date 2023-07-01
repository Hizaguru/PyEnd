# Flask Image Upload Admin Panel

This Flask project is an admin panel for uploading images to a database. Follow the instructions below to easily set it up for personal use.

## Prerequisites

Before getting started, ensure that you have the following installed on your computer:

- Python 3
- pip3
- MySQLdb

## Installation

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/your-username/flask-image-upload-admin-panel.git
   ```

2. Navigate to the project directory:

   ```
   cd flask-image-upload-admin-panel
   ```

3. Create a `.env` file and paste the contents from the `env.data` file. Add your own credentials to the first two lines of the `.env` file.

4. Create a virtual environment in the `PyEnd/` directory:

   ```
   python3 -m venv venv
   ```

5. Activate the virtual environment:

   ```
   source venv/bin/activate
   ```

6. Install the project dependencies:

   ```
   pip3 install -r requirements.txt
   ```

## Database Setup

1. Ensure that your MySQL database is running.

2. Open the `database.sql` file and copy each line.

3. Paste the copied lines into your MySQL database to create the necessary tables.

## Running the Project

To run the Flask project, execute the following command within the `PyEnd/` folder:

```
flask run
```

This command will start the Flask development server, and the admin panel will be accessible at [http://localhost:5000](http://localhost:5000).

Please make sure that the MySQL database is running before starting the project.

## Contributing

Contributions to the Flask Image Upload Admin Panel are welcome! If you encounter any issues or have suggestions for improvements, please feel free to create an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

Please copy and paste this Markdown-formatted content into your `README.md` file, and it should render correctly when viewed on platforms that support Markdown formatting.