from flask import Flask, flash, redirect, request, session, jsonify
from flask import render_template
import logging

app = Flask(__name__)
app.debug = True
app.secret_key = b'[Le\x1e\xd1\x9cE3\xed\xcb\xfdC\xc7\x1cd\x04'   
app.run(host='0.0.0.0', port=5000, debug=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/sign", methods=["POST"])
def sign():
    username = request.form['username']
    password = request.form['password']
    if username == "admin" and password == "123":
        session["usuario"] = username
        user = jsonify({ 'username': username }, { 'user': session["usuario"] } ), 201 , {'ContentType':'application/json'}
        logging.error(user)
        print (user)

        return  redirect("/profile")
    else:
        flash("Correo o contraseña incorrectos"), 400
        logging.error(session)
        print(session)
        return redirect("/login")
 
@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.before_request
def before_request():
    ruta = request.path
    if not 'usuario' in session and ruta != "/login" and ruta != "/"  and not ruta.startswith("/static"):
        flash("Inicia sesión para continuar")
        return redirect("/login")
