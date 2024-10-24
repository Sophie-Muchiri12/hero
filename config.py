# import os

# class Config:
#     # Database configuration
#     SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///heroes.db')  # Use environment variable or default to SQLite
#     SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable track modifications feature

#     # Additional configurations can be added here
#     DEBUG = os.getenv('DEBUG', 'True') == 'True'  # Enable or disable debug mode

#     # You can add other configurations like session secret keys, API keys, etc.
#     SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')  # Change this for production
