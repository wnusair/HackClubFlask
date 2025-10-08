from flask import Flask, render_template, request, flash, redirect, url_for

import csv

app = Flask(__name__)
app.secret_key = ";lkfaofiewqjfojdsafjsa"

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        full_name = request.form.get("full_name")
        email = request.form.get("email")

        with open("accounts.csv", "a") as file:
            file.write(f"{username},{password},{full_name},{email}\n")
        

    return render_template("register.html")

@app.route('/login', methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        with open("accounts.csv", "r", newline="") as file:
            csv_reader = csv.reader(file)

            for row in csv_reader:
                if row[3] == email and row[1] == password:
                    print("account matched", email, password)
                else:
                    print("did not match")
                    print(row[3], email, row[1], password)

    return render_template("login.html")

app.run('0.0.0.0')