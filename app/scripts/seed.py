from app.shop.models import Category, Recipe
from app.extensions.database import db
from flask import Blueprint
from app.simple_pages.models import Work


seed_blueprint = Blueprint("seed", __name__)


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
    print("test1")
    for key, category in category_data.items():
        print(key)
        new_category = Category( name=category['name'])
        print(new_category)
        new_category.save()

    print("test2")
    # for key, recipe in recipe_data.items():
    #     new_recipe = Recipe(name=recipe['name'], content=recipe['content'], category_id=recipe['category_id'])
    #     db.session.add(new_recipe)

    db.session.commit()
    return "Added categories"

@seed_blueprint.route('/delete-seed')
def delete_seed():
    categories = Category.query.all()
    for category in categories:
        category.delete()
    
    recipes = Recipe.query.all()
    for recipe in recipes:
        recipe.delete()
    
    works = Work.query.all()
    for work in works:
        work.delete()

    return "Deleted seed"