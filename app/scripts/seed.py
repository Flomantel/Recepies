from app.app import create_app
from app.shop.models import Category, Recipe
from app.extensions.database import db
from flask import Blueprint

seed_blueprint = Blueprint("seed", __name__)

if __name__ == '__main__':
    app = create_app()
    app.app_context().push()


category_data = {
    'starter' : {'name': 'Starter'},
    'fish' : {'name': 'Fish'},
    'meat' : {'name': 'Meat'},
    'soup' : {'name': 'Soup'},
    'vegan' : {'name': 'Vegan'},
    'vegetarian' : {'name' : 'Vegetarian'},
    'dessert' : {'name' : 'Dessert'},
}

recipe_data = {
    'cookies' : {'name': 'Cookies', 'content': '200gr. soft butter, 50gr. sugar, 50gr. brown sugar, pinch of salt, 230gr. flour, 1tsp baking powder, 3 eggs, make the dought/ roll/ calendula, cut if necessary and bake it by 180 degreed / 8-10min', 'category_id': 7 }
}

@seed_blueprint.route('/seed')
def seed():
    for key, category in category_data.items():
        new_category = Category( name=category['name'])
        db.session.add(new_category)

    db.session.commit()

    for key, recipe in recipe_data.items():
        new_recipe = Recipe(name=recipe['name'], content=recipe['content'], category_id=recipe['category_id'])
        db.session.add(new_recipe)

    db.session.commit()
    return "OK"
