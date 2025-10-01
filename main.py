from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "shamgar" and password == "shamgar":
            print("correct")
        else:
            print("you are a hacker")


    shamgar = "cool"

    return render_template("index.html", x=2, shamgar=shamgar)

app.run('0.0.0.0')