from app.shop.models import Recipe, Category

def test_index_success(client):
    response = client.get('/')
    assert response.status_code == 200

def test_profession_redirects(client):
    response = client.get('/profession')
    assert response.status_code == 200

def test_flo_ma_redirects(client):
    response = client.get('/flo-ma')
    assert response.status_code == 200

def test_recipes_renders_recipes(client):
    response = client.get('/category/1')
    assert b'Cookies' in response.data

def test_recipe_render_recipe(client):
    new_recipe = Recipe(content="jkasdf", name="Croissant", category_id=7)
    new_recipe.save()
    response = client.get('/category/7')
    print(response.data)
    new_recipe.delete()
    assert b'Cookies' in response.data
