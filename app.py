import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from blueprints.main import main_bp
from blueprints.auth import auth_bp

# Initialize Flask application
app = Flask(__name__)

# Load the SECRET_KEY from environment variables
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')

# Configure the URI for connecting to the PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/glow_spa'
db = SQLAlchemy(app)

# Register blueprints for routing
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)

# Initialize the Flask application
if __name__ == '__main__':
    with app.app_context():
        # Create database tables
        db.create_all()

    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=8080)
