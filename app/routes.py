from flask import (
    render_template,
    url_for,
    redirect,
)
from app import app

@app.route("/", methods=["GET"])
def parking():
    return render_template("parking.pug")
