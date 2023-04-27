from flask import Blueprint, render_template, send_file, request
from .models import Work
from app.shop.models import Category
from app.scripts.seed import seeding
import json

blueprint = Blueprint("work", __name__)


@blueprint.route("/profession")
def profession():
    work = Work.query.all()
    return render_template("list.html", work=work)


@blueprint.route("/flo-ma")
def flo_ma():
    return render_template("about.html")


# @blueprint.route("/run-seed")
# def run_seed():
#     seeding()
#     category = Category.query.all()
#     new_dict = {}
#     x = 0
#     for item in category:
#         new_dict[f"{x}"] = item.id
#         x +=1
#         print(item.id)
#     return json.dumps(new_dict)
