from flask import Flask, redirect, url_for, request, render_template, jsonify, send_file
from jinja2 import Template
import csv
from collections import defaultdict
from flask_login import login_user, logout_user, login_required
import requests

app = Flask(__name__)
log = 0


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
        if user:
            if user == pass1:
                global log
                log = 1
                return redirect(url_for("dashboard"))
            else:
                return render_template("login.html", result=flash_data)
        else:
            return render_template("login.html", result=flash_data)


@app.route("/dashboard/<machine_name>")
def machine_detail_api_call(machine_name):
    if log == 0:
        return render_template("login.html")
    else:
        dec = defaultdict(list)
        with open("data/Dec-2020/" + machine_name + ".csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                for (k, v) in row.items():
                    dec[k].append(v)

        jan = defaultdict(list)
        with open("data/Jan-2021/" + machine_name + ".csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                for (k, v) in row.items():
                    jan[k].append(v)

        feb = defaultdict(list)
        with open("data/Feb-2021/" + machine_name + ".csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                for (k, v) in row.items():
                    feb[k].append(v)

        mar = defaultdict(list)
        with open("data/March-2021/" + machine_name + ".csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                for (k, v) in row.items():
                    mar[k].append(v)
        # print(columns["PERIOD"][9])
        print(mar["OPERATE Time"][7])
        # desired_array = map(int, columns["Period"][8])
        # print(desired_array)
        name = machine_name.replace("_", " ")
        name = name.replace("m", "M")
        name = name.replace("data", " ")
        return render_template(
            "dashboard.html", data=dec, data1=jan, data2=feb, data3=mar, mname=name
        )


@app.route("/dashboard")
def dashboard():
    if log == 0:
        return render_template("login.html")
    else:
        columns = defaultdict(list)
        with open("data/Dec-2020/machine_data_1.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                for (k, v) in row.items():
                    columns[k].append(v)
        jan = defaultdict(list)
        with open("data/Jan-2021/machine_data_1.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                for (k, v) in row.items():
                    jan[k].append(v)

        feb = defaultdict(list)
        with open("data/Feb-2021/machine_data_1.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                for (k, v) in row.items():
                    feb[k].append(v)

        mar = defaultdict(list)
        with open("data/March-2021/machine_data_1.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                for (k, v) in row.items():
                    mar[k].append(v)
        print(columns["OPERATE Time"][7])
        return render_template(
            "dashboard.html",
            data=columns,
            data1=jan,
            data2=feb,
            data3=mar,
            mname="Machine 1",
        )


@app.route("/download/<machine_name>")
def machine_detail_download_api_call(machine_name):
    path = "./downloads/" + machine_name + ".xls"
    return send_file(path, as_attachment=True)


@app.route("/test")
def multi_month_machine_data():
    columns = defaultdict(list)
    with open("data/Dec-2020/machine_data_1.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for (k, v) in row.items():
                columns[k].append(v)
    print(columns["PERIOD"][7])
    print(columns["OPERATE Time"][7])
    return columns


@app.route("/download")
def download():
    return render_template("download.html")


if __name__ == "__main__":
    app.run(debug=True)
