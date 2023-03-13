from flask import Flask, redirect, url_for, render_template, send_file

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    merch_data = {
'shirt' : {'name': 'T-shirt', 'price': '220.00€'},
'short' : {'name': 'Short', 'price': '80.00€'},
'cap'   : {'name': 'Truckercap', 'price': '45.00€'},
'backbag': {'name': 'Backbag', 'price': '120.00€'},
    }

    return render_template('index.html', merch = merch_data)

@app.route('/flo-ma')
def flo_ma():
    return render_template('about.html')

@app.route('/profession')
def profession():
    work_data = {
'hotel-mercure' : {'name': 'Hotel Mercure', 'employed-as': 'Trainee'},
'alte-mainmühle' : {'name': 'Alte Mainmühle', 'employed-as': 'Commi de Cuisine'},
'parkhotel-wallgau' : {'name': 'Parkhotel Wallgau', 'employed-as': 'Commi de Cuisine'},
'die-bank' : {'name': 'Die Bank', 'employed-as': 'Commi de Cuisine'},
'wiener-botschaft' : {'name': 'Wiener-Botschaft', 'employed-as': 'Demi Chef de Cuisine'},
'les-cuisiners' : {'name': 'Les Cuisiners', 'employed-as': 'Demi Chef de Cuisine'},
'geisels-werneckhof' : {'name': 'Geisels Werneckhof *', 'employed-as': 'Demi Chef de Cuisine'},
'hotel-königshof' : {'name': 'Hotel Königshof *', 'employed-as': 'Demi Chef de Cuisine'},
'käfer-schänke' : {'name': 'Käfer Schänke', 'employed-as': 'Chef de Partie'},
'schmelzwerk' : {'name': 'Schmelzwerk', 'employed-as': 'Chef de Partie'},
'schmelzwerk' : {'name': 'Schmelzwerk', 'employed-as': 'Chef de Cuisine'},
}
    return render_template('list.html', work = work_data)

@app.route('/contact')
def contact():
    return send_file('static/download/contact.txt', as_attachment=True)

@app.route('/shop/<slug>')
def shop(slug):
    merch_data = {
'shirt' : {'name': 'T-shirt', 'price': '220.00€'},
'short' : {'name': 'Short', 'price': '80.00€'},
'cap'   : {'name': 'Truckercap', 'price': '45.00€'},
'backbag': {'name': 'Backbag', 'price': '120.00€'},
    }

    if slug in merch_data:
        return '<h1>' + merch_data[slug]['name'] + '</h1>' +  '<p>' + merch_data[slug]['price'] + '</p>' + 'all our products are fair trade and sustainable - the product comes with our logo and a picture of Florian :)'
    else:
        return 'Sorry we could not find that merch. Please try out /shirt, /short, /cap, /backbag'
    


if __name__=='__main__':
    app.run(port=8000, debug=True)