

from flask import Flask
from models import db, Restaurant, Pizza

app = Flask(__name__)



app.app_context().push()
db.init_app(app)
db.create_all()

def seed_data():
    
    restaurant1 = Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue")
    restaurant2 = Restaurant(name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100")

    
    pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    
    restaurant1.pizzas.append(pizza1)
    restaurant2.pizzas.append(pizza1)
    restaurant2.pizzas.append(pizza2)


    db.session.add(restaurant1)
    db.session.add(restaurant2)
    db.session.add(pizza1)
    db.session.add(pizza2)

    
    db.session.commit()

if __name__ == '__main__':
    seed_data()


   