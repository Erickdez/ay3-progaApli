from flask import Flask, render_template, request, redirect, session
from logic.client_logic import ClientLogic
import bcrypt

app = Flask(__name__)
app.secret_key = "Bad1secret2key3!+"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def registerClient():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        logic = ClientLogic()
        clientName = request.form["name"]
        clientEmail = request.form["email"]
        clientCel = request.form["cel"]
        passwd = request.form["passwd"]
        confpasswd = request.form["confpasswd"]
        if passwd == confpasswd:
            salt = bcrypt.gensalt(rounds=14)
            strSalt = salt.decode("utf-8")
            encPasswd = passwd.encode("utf-8")
            hashPasswd = bcrypt.hashpw(encPasswd, salt)
            strPasswd = hashPasswd.decode("utf-8")
            rows = logic.insertClient(clientName, clientCel, clientEmail, strPasswd, strSalt)
            return redirect("login")
        else:
            return redirect("register")
        return f"posted register rows: {rows}"


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        logic = ClientLogic()
        clientEmail = request.form["email"]
        passwd = request.form["passwd"]
        userDict = logic.getClientByEmail(clientEmail)
        salt = userDict["salt"].encode("utf-8")
        hashPasswd = bcrypt.hashpw(passwd.encode("utf-8"), salt)
        dbPasswd = userDict["password"].encode("utf-8")
        if hashPasswd == dbPasswd:
            session["login_email"] = clientEmail
            session["login_name"] = userDict["name"]
            session["loggedIn"] = True
            return redirect("dashboard")
        else:
            return redirect("login")
        return "posted login"


@app.route("/logout")
def logout():
    if session.get("loggedIn"):
        session.pop("login_user")
        session.pop("loggedIn")
        return redirect("login")
    else:
        return redirect("login")


@app.route("/dashboard")
def dashboard():
    if session.get("loggedIn"):
        user = session.get("login_name")
        return render_template("dashboard.html", user=user)
    else:
        return redirect("login")


if __name__ == "__main__":
    app.run(debug=True)
