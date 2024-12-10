from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the Flask app
app = Flask(__name__)

# Load configuration from the .env file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'mysql://root:rootpassword@db:3306/travel_guide')

# Initialize the database
db = SQLAlchemy(app)

# Define the Location model
class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<Location {self.name}>'

# Home route - Displays all locations
@app.route('/')
def home():
    locations = Location.query.all()
    return render_template('home.html', locations=locations)

# Destination route - Displays a specific location's details
@app.route('/destination/<int:id>')
def destination(id):
    location = Location.query.get(id)
    return render_template('destination.html', location=location)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
