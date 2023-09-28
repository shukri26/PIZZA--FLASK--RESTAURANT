Running the Application
To run the Flask server and test the API endpoints:
    
    set-up steps:

Clone the repository
git clone https://github.com/shukri26/PIZZA--FLASK--RESTAURANT
cd PIZZA--FLASK--RESTAURANT
Create a virtual environment and activate it:



python -m venv venv
source venv/bin/activate  # On Windows,  `venv\Scripts\activate`
Install dependencies:


pip install -r requirements.txt
Initialize the database and apply migrations:


python manage.py db init
python manage.py db migrate
python manage.py db upgrade
Start the Flask application:


License

MINT