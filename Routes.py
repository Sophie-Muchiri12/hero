from flask import jsonify,request

from database import db
from models.heroes import Hero
from models.powers import Power
from models.hero_powers import HeroPower




def create_routes(app):
    
    # Route to get all heroes
    @app.route('/heroes', methods=['GET'])
    def get_heroes():
        heroes = Hero.query.all()
        return jsonify([hero.to_dict() for hero in heroes])

    # Route to get a specific hero along with their powers
    @app.route('/heroes/<int:id>', methods=['GET'])
    def get_hero(id):
        hero = Hero.query.get(id)  # Get the hero by ID
        if hero is None:
            return jsonify({"error": "Hero not found"}), 404  # Return error if not found

        # Fetch associated hero powers
        hero_powers = HeroPower.query.filter_by(hero_id=hero.id).all()

        # Create a list of powers associated with the hero
        hero_powers_list = []
        for hero_power in hero_powers:
            power = Power.query.get(hero_power.power_id)  # Fetch the actual Power
            if power:  # Check if the power exists
                hero_powers_list.append({
                    "hero_id": hero_power.hero_id,
                    "id": hero_power.id,
                    "power": {
                        "description": power.description,
                        "id": power.id,
                        "name": power.name
                    },
                    "power_id": hero_power.power_id,
                    "strength": hero_power.strength
                })

        # Construct the response in the specified format
        response = {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "hero_powers": hero_powers_list  # Ensure powers are correctly included
        }

        return jsonify(response)

    # Route to create a new hero
    @app.route('/heroes', methods=['POST'])
    def create_hero():
        data = request.json
        new_hero = Hero(name=data['name'], super_name=data['super_name'])
        db.session.add(new_hero)
        db.session.commit()
        return jsonify(new_hero.to_dict()), 201

    # Route to get all powers
    @app.route('/powers', methods=['GET'])
    def get_powers():
        powers = Power.query.all()
        return jsonify([power.to_dict() for power in powers])

    # Route to get a specific power
    @app.route('/powers/<int:id>', methods=['GET'])
    def get_power(id):
        power = Power.query.get(id)
        if power is None:
            return jsonify({"error": "Power not found"}), 404
        return jsonify(power.to_dict())

    # Route to update an existing power
    @app.route('/powers/<int:id>', methods=['PATCH'])
    def update_power(id):
        power = Power.query.get(id)
        if power is None:
            return jsonify({"error": "Power not found"}), 404
        
        data = request.json
        if "description" in data:
            power.description = data["description"]
            db.session.commit()
            return jsonify(power.to_dict())
        
        return jsonify({"errors": ["validation errors"]}), 400

    # Route to create a new hero-power relationship
    @app.route('/hero_powers', methods=['POST'])
    def create_hero_power():
        data = request.json
        
        # Ensure the hero and power exist before creating the relationship
        hero = Hero.query.get(data['hero_id'])
        power = Power.query.get(data['power_id'])

        if hero is None:
            return jsonify({"error": "Hero not found"}), 404
        if power is None:
            return jsonify({"error": "Power not found"}), 404
        
        new_hero_power = HeroPower(
            strength=data['strength'],
            hero_id=data['hero_id'],
            power_id=data['power_id']
        )
        db.session.add(new_hero_power)
        db.session.commit()

        # Return the created hero-power relationship with associated hero and power details
        response = {
            "id": new_hero_power.id,
            "hero_id": new_hero_power.hero_id,
            "power_id": new_hero_power.power_id,
            "strength": new_hero_power.strength,
            "hero": {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name
            },
            "power": {
                "id": power.id,
                "name": power.name,
                "description": power.description
            }
        }

        return jsonify(response), 201



