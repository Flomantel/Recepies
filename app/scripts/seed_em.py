from app.extensions.database import db
from app.simple_pages.models import Work
from flask import Blueprint

seed_em_blueprint = Blueprint("seed_em", __name__)

work_data = {
    "hotel-mercure": {"name": "Hotel Mercure", "employed-as": "Trainee"},
    "alte-mainmühle": {"name": "Alte Mainmühle", "employed-as": "Commi de Cuisine"},
    "parkhotel-wallgau": {
        "name": "Parkhotel Wallgau",
        "employed-as": "Commi de Cuisine",
    },
    "die-bank": {"name": "Die Bank", "employed-as": "Commi de Cuisine"},
    "wiener-botschaft": {
        "name": "Wiener-Botschaft",
        "employed-as": "Demi Chef de Cuisine",
    },
    "les-cuisiners": {"name": "Les Cuisiners", "employed-as": "Demi Chef de Cuisine"},
    "geisels-werneckhof": {
        "name": "Geisels Werneckhof *",
        "employed-as": "Demi Chef de Cuisine",
    },
    "hotel-königshof": {
        "name": "Hotel Königshof *",
        "employed-as": "Demi Chef de Cuisine",
    },
    "käfer-schänke": {"name": "Käfer Schänke", "employed-as": "Chef de Partie"},
    "schmelzwerk": {"name": "Schmelzwerk", "employed-as": "Chef de Partie"},
    "schmelzwerk": {"name": "Schmelzwerk", "employed-as": "Chef de Cuisine"},
}

# @seed_em_blueprint.route("/seed_em")
# def seed_em():
#     for key, value in work_data.items():
#         new_work = Work(name=value['name'], employed=value['employed-as'])
#         db.session.add(new_work)
#     db.session.commit()

#     return "OK"