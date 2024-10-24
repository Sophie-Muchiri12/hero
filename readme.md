# Project Title

Superheroes API

## Project Description

The Superheroes API is a RESTful web service that allows users to interact with a database of superheroes and their powers. This project showcases how to build a complete web application using Flask, SQLAlchemy, and Flask-Migrate. The API provides endpoints for retrieving hero data, powers, and relationships between them, making it an excellent resource for developers interested in understanding how to work with Flask and RESTful principles.

### Features:
- Retrieve a list of all heroes and their details.
- Get specific hero information by ID.
- Access a list of available superpowers.
- Update power descriptions.
- Create relationships between heroes and their powers.

### Technologies Used:
- **Flask**: A lightweight WSGI web application framework.
- **SQLAlchemy**: An ORM that simplifies database interaction.
- **Flask-Migrate**: A tool for handling SQLAlchemy database migrations.
- **SQLite**: A simple database for development purposes.

### Challenges Faced:
- Managing circular imports while structuring the application.
- Ensuring data validation and error handling were robust.
- Implementing relationships between models effectively.



## How to Install and Run the Project

1. **Clone the repository:**

   git clone <repository-url>
   cd superheroes
### Create a virtual environment:

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


### Set up the database:

flask db init
flask db migrate -m "Initial migration."
flask db upgrade
### Run the application:
flask run / python app.py
### How to Use the Project
Once the server is running, you can interact with the API using any API client like Postman or curl.

Example Endpoints:
### Get all heroes:
GET http://127.0.0.1:5000/heroes
### Get hero by ID:

GET http://127.0.0.1:5000/heroes/1
### Get all powers:
GET http://127.0.0.1:5000/powers
### Update a power:
PATCH http://127.0.0.1:5000/powers/1
Content-Type: application/json

{
  "description": "Updated description for super strength"
}
### Create a hero power:
POST http://127.0.0.1:5000/hero_powers
Content-Type: application/json

{
  "strength": "Average",
  "power_id": 1,
  "hero_id": 3
}