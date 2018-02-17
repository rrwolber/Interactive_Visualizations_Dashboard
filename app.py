# Import dependencies
from flask import Flask, render_template, jsonify, request, redirect
from model import session, Pet, func
import requests
import sqlite3 as sql

#Flask Setup
app = Flask(__name__)


#Main Route
@app.route('/')
def home():
    return render_template('index.html')

