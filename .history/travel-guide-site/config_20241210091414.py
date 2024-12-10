import os

# Set the secret key for session management
SECRET_KEY = os.urandom(24)

# Database URI for Flask-SQLAlchemy
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://user:userpass@db/travel_guide')
SQLALCHEMY_TRACK_MODIFICATIONS = False
