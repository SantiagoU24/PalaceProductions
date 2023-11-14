from flask import Flask
from flask_mysqldb import MySQLdb, MySQL
import os

app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='PalaceProductions'
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql = MySQL(app)