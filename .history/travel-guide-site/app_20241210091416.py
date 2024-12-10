from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the Flask app
app = Flask(__name__)

# Configure the app to use the MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mysql+pymysql://user:userpass@db/travel_guide')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Destination model
class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(200), nullable=True)

# Route for the homepage
@app.route('/')
def home():
    destinations = Destination.query.all()  # Fetch all destinations from the database
    return render_template('home.html', destinations=destinations)

# Route for a specific destination
@app.route('/destination/<int:id>')
def destination(id):
    destination = Destination.query.get_or_404(id)  # Fetch destination by ID
    return render_template('destination.html', destination=destination)

if __name__ == '__main__':
    app.run(debug=True)
