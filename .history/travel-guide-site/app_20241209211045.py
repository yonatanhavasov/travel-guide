from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'SQLALCHEMY_DATABASE_URI', 
    'mysql+pymysql://root:root_password@db/travel_guide'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Models
class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Destination {self.name}>'

# Routes
@app.route('/')
def home():
    destinations = Destination.query.all()
    return render_template('home.html', destinations=destinations)

@app.route('/destination/<int:id>')
def destination_detail(id):
    destination = Destination.query.get_or_404(id)
    return render_template('destination.html', destination=destination)

@app.route('/add', methods=['GET', 'POST'])
def add_destination():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        image_url = request.form['image_url']

        new_destination = Destination(name=name, description=description, image_url=image_url)
        db.session.add(new_destination)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template('add_destination.html')

@app.route('/weather', methods=['GET'])
def weather():
    # Example route for weather data integration
    city = request.args.get('city', 'Tel Aviv')
    weather_data = {
        'city': city,
        'temperature': '25°C',
        'description': 'Sunny'
    }
    return render_template('weather.html', weather=weather_data)

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

