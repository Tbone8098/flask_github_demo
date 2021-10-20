from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
# from flask_app.models import 

@app.route('/user/new')
def new_user():
    return 'new user'

@app.route('/user/create', methods=['post'])
def create_user():
    print(request.form)
    return 'create user'

@app.route('/user/<int:id>')
def show_user(id):
    return 'show user'

@app.route('/user/<int:id>/edit')
def edit_user(id):
    return 'edit user'

@app.route('/user/<int:id>/update', methods=['post'])
def update_user(id):
    return 'update user'

@app.route('/user/<int:id>/delete')
def delete_user(id):
    return 'delete user'