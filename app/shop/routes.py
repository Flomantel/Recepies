from app.extensions.database import db
from flask import Blueprint, render_template, request, flash, abort, redirect
from .models import Category, Recipe
import json


blueprint = Blueprint('recipe',__name__)



@blueprint.route('/category/<id>')
def category(id):
    page_number = request.args.get('page', 1, type=int)
    recipe_pagination = Recipe.query.filter_by(category_id=id).paginate(page=page_number, per_page=4)
    category = Category.query.filter_by(id=id).first_or_404()
    return render_template('shop/show.html', category=category, recipe_pagination=recipe_pagination)

@blueprint.route('/category/<id>/delete', methods=['POST', 'DELETE'])
def delete_item(id):
    if request.method == 'POST':
        #print(request.form.to_dict()["_method"])
        recipe = Recipe.query.filter_by(id=request.form.to_dict()["_method"]).first()
        recipe.delete()
        db.session.commit()
        flash('Recipe deleted')
        return redirect(f"/category/{id}")
    else:
        abort(405)
    

@blueprint.route('/')
def index():
    category = Category.query.all()
    return render_template('index.html', category=category)

@blueprint.get('/form')
def get_form():
    return render_template('shop/form.html')

@blueprint.post('/form')
def post_form():

    category_id_number = get_category_number(request.form.get('category_id'))

    recipe = Recipe(
        name=request.form.get('name'),
        content=request.form.get('content'),
        category_id=category_id_number,
    )
    recipe.save()
    db.session.commit() 

    return redirect("/")

@blueprint.get ('/edit/<id>')
def edit(id):
    data = Recipe.query.filter_by(id=id).first()
    return render_template('shop/edit.html', recipe=data)

@blueprint.post('/edit/<id>')
def update(id):

    category_id_number = get_category_number(request.form.get('category_id'))

    recipe = Recipe.query.filter_by(id=id).first()
    recipe.name = request.form.get('name')
    recipe.content = request.form.get('content')
    recipe.category_id = category_id_number
    recipe.save()
    db.session.commit()
    return redirect('/')


def get_category_number(category_name): 
    category_id_number = 0
    if category_name == "Starter":
        category_id_number = 1
    elif category_name == "Fish":
        category_id_number = 2
    elif category_name == "Meat":
        category_id_number = 3
    elif category_name == "Soup":
        category_id_number = 4
    elif category_name == "Vegan":
        category_id_number = 5
    elif category_name == "Vegetarian":
        category_id_number = 6
    elif category_name == "Dessert":
        category_id_number = 7
    return category_id_number


