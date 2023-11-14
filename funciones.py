from flask import Flask, render_template, request, redirect, url_for, session, Response
import os
import database 
from flask_mysqldb import MySQLdb, MySQL
import os
from app import *

app = Flask(__name__, template_folder=('templates'), static_folder='static')

mysql=MySQL(app)

#LOGIN

def login(request):
    if request.method == 'POST' and 'txtCorreo' in request.form and 'txtPassword' in request.form:
        _correo = request.form['txtCorreo']
        _password = request.form['txtPassword']

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM usuarios WHERE correo = %s AND contrasena = %s', (_correo, _password,))
        account = cur.fetchone()

        if account:
            session['logueado'] = True
            session['id'] = account['id_usuario']
            return True  # Autenticación exitosa
    return False  # Autenticación fallida

