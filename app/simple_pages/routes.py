from flask import Blueprint, render_template, send_file, request
from .models import Work

blueprint = Blueprint("work", __name__)



@blueprint.route("/profession")
def profession():
    work = Work.query.all()
    return render_template("list.html", work=work)


@blueprint.route("/flo-ma")
def flo_ma():
    return render_template("about.html")


@blueprint.route("/contact")
def contact():
    return send_file("../static/download/contact.txt", as_attachment=True)
