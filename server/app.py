from flask import Flask, jsonify, request, abort
from models import db, Restaurant, Pizza, RestaurantPizza
from flask_migrate import Migrate


app = Flask(__name__)

db.init_app(app)
migrate = Migrate(app, db)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    restaurant_list = [
        {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
        }
        for restaurant in restaurants
    ]
    return jsonify(restaurant_list)


@app.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

    pizzas = [
        {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients,
        }
        for pizza in restaurant.pizzas
    ]

    restaurant_data = {
        "id": restaurant.id,
        "name": restaurant.name,
        "address": restaurant.address,
        "pizzas": pizzas,
    }
    return jsonify(restaurant_data)


@app.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if not restaurant:
        return jsonify({"error": "Restaurant not found"}), 404

  
    RestaurantPizza.query.filter_by(restaurant_id=restaurant_id).delete()
    db.session.delete(restaurant)
    db.session.commit()

    return "", 204


@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    pizza_list = [
        {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients,
        }
        for pizza in pizzas
    ]
    return jsonify(pizza_list)


@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()

    price = data.get("price")
    pizza_id = data.get("pizza_id")
    restaurant_id = data.get("restaurant_id")

    
    if price is None or pizza_id is None or restaurant_id is None:
        return jsonify({"errors": ["price, pizza_id, and restaurant_id are required"]}), 400

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    if not pizza or not restaurant:
        return jsonify({"errors": ["Pizza or Restaurant not found"]}), 404

    
    restaurant_pizza = RestaurantPizza(price=price, pizza=pizza, restaurant=restaurant)

    db.session.add(restaurant_pizza)
    db.session.commit()

    
    return jsonify({
        "id": pizza.id,
        "name": pizza.name,
        "ingredients": pizza.ingredients,
    }), 201

if __name__ == '__main__':
    app.run(debug=True)
