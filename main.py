from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = ";lkfaofiewqjfojdsafjsa"

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "shamgar" and password == "shamgar":
            flash("Success")
            return redirect(url_for("success"))
        else:
            flash("Failed")
            return redirect(url_for("fail"))


    shamgar = "cool"

    return render_template("index.html", x=2, shamgar=shamgar)

@app.route('/success')
def success():
    return render_template("success.html")

@app.route('/fail')
def fail():
    return render_template("fail.html")


app.run('0.0.0.0')