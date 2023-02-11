from flask import render_template, request
from flask_application import app, db
from .models import Checker, Slider


@app.route("/", methods=("GET", "POST"))
@app.route("/index", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        current = request.form["current"]
        current2 = request.form["current2"]
        current3 = request.form["current3"]
        return render_template("index.html")
    return render_template("index.html")


@app.route("/slider_update", methods=["POST", "GET"])
def slider():
    received_data = request.data
    # received_data = float(received_data) / 50
    received_data = float(received_data)
    db_sesssion = Slider.query.first()
    db_sesssion.slider = f"{received_data}"
    db.session.commit()
    return str(received_data * 50)


@app.route("/slider_update2", methods=["POST", "GET"])
def slider2():
    received_data = request.data
    received_data = float(received_data)
    db_sesssion = Slider.query.first()
    db_sesssion.slider2 = f"{received_data}"
    db.session.commit()
    return str(received_data)


@app.route("/slider_update3", methods=["POST", "GET"])
def slider3():
    received_data = request.data
    received_data = float(received_data)
    db_sesssion = Slider.query.first()
    db_sesssion.slider3 = f"{received_data}"
    db.session.commit()
    return str(received_data)


@app.route("/check_update", methods=["POST", "GET"])
def check():
    received_data = request.data
    received_data = str(received_data).replace("'", "")[1:]
    db_sesssion = Checker.query.first()
    db_sesssion.check = f"{received_data}"
    db.session.commit()
    return received_data


@app.route("/check_update2", methods=["POST", "GET"])
def check2():
    received_data = request.data
    received_data = str(received_data).replace("'", "")[1:]
    db_sesssion = Checker.query.first()
    db_sesssion.check2 = f"{received_data}"
    db.session.commit()
    return received_data


@app.route("/check_update3", methods=["POST", "GET"])
def check3():
    received_data = request.data
    received_data = str(received_data).replace("'", "")[1:]
    db_sesssion = Checker.query.first()
    db_sesssion.check3 = f"{received_data}"
    db.session.commit()
    return received_data


@app.route("/check_update4", methods=["POST", "GET"])
def check4():
    received_data = request.data
    received_data = str(received_data).replace("'", "")[1:]
    db_sesssion = Checker.query.first()
    db_sesssion.check4 = f"{received_data}"
    db.session.commit()
    return received_data
