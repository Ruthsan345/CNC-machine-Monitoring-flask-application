from flask import Flask, redirect, url_for, request, render_template, jsonify
from jinja2 import Template
import csv
from collections import defaultdict
from flask_login import login_user, logout_user, login_required

app = Flask(__name__)
log = 1


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/logout")
def logout():
    global log
    log = 0
    return render_template("login.html")


@app.route("/login_post", methods=["POST", "GET"])
def login_post():
    flash_data = "error"
    if request.method == "POST":
        user = request.form["email"]
        pass1 = request.form["password"]
        if user == pass1:
            global log
            log = 1
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", result=flash_data)


@app.route("/dashboard/<machine_name>")
def machine_detail_api_call(machine_name):
    if log == 0:
        return render_template("login.html")
    else:
        columns = defaultdict(list)
        with open("data/" + machine_name + ".csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                for (k, v) in row.items():
                    columns[k].append(v)
        print("hi")
        # print(columns["PERIOD"][9])
        print(columns["OPERATE Time"][7])
        # desired_array = map(int, columns["Period"][8])
        # print(desired_array)
        return render_template("dashboard.html", data=columns)


@app.route("/dashboard")
def dashboard():
    if log == 0:
        return render_template("login.html")
    else:
        columns = defaultdict(list)
        with open("data/machine_data_1.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                for (k, v) in row.items():
                    columns[k].append(v)
        print(columns["PERIOD"][7])
        print(columns["OPERATE Time"][7])
        return render_template("dashboard.html", data=columns)


if __name__ == "__main__":
    app.run(debug=True)
