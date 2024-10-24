from flask import Flask
from flask_migrate import Migrate
from database import db
from Routes import  create_routes



app = Flask(__name__)

# Database configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Register routes
create_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
