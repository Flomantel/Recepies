from app.extensions.database import db
from app.shop.models import Recipe

def test_recipe_update(client):
    recipe = Recipe(content='jkasdf', name='Croissant', category_id=1)
    db.session.add(recipe)
    db.session.commit()


    recipe.name ='Potato'
    recipe.save()

    updated_recipe = Recipe.query.filter_by(name='Potato').first()
    recipe.delete()
    assert updated_recipe.name == 'Potato'

def test_recipe_delete(client):
    recipe = Recipe(content='jkasdf', name='Croissant', category_id=2)
    db.session.add(recipe)
    db.session.commit()

    recipe.delete()

    deleted_recipe = Recipe.query.filter_by(content='jkasdf', name = 'Croissant', category_id=2).first()
    assert deleted_recipe is None

def test_get_form_renders(client):
    response = client.get('/form')
    print(response.data)
    assert b'Name of the recipe' in response.data


def test_post_form_create_recipe(client):
    response = client.post('shop/form', data={
        'name' : 'Croissants',
        'content': 'jaskfho',
        'category_id': '2'
    })

    assert Recipe.query.first() is not None

def test_post_form_create_content(client):
    response = client.post('/form', data={
        'name' : 'Croissants',
        'content' : 'jaskfho',
        'category_id' : '7'
    })

    assert Recipe.query.first().category_id is 7