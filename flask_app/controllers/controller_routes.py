from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
# from flask_app.models import 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    # dashboard is ready to go!
    return render_template('dashboard.html')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'page not found'