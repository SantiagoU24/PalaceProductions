from flask import Flask, render_template, request, redirect, url_for
import os
import database as db
from funciones import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

#FUNCION DEL LOGIN

@app.route('/login', methods=["GET", "POST"])
def login_route():
    if request.method == 'POST':
        if login(request=True):
            return render_template("admin.html")
        else:
            return render_template('login.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')




#------------------------------

if __name__ == '__main__':
    app.run(debug = True, port=4000)