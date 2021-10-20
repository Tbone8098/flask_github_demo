from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE_SCHEMA
import re

class User:
    def __init__(self, data):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# C ************************************************
# C ************************************************
# C ************************************************
 
    @classmethod
    def create(cls, **data):
        query = 'INSERT INTO users (first_name) VALUES (%(first_name)s)'
        new_users_id = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)

        return new_users_id
    
# R ************************************************
# R ************************************************
# R ************************************************
 
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query)
        if len(results):
            all_users = []
            for users in results:
                all_users.append(cls(users))
            return all_users

    @classmethod
    def get_one(cls, **data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)
        if not results:
           return results
        return cls(results[0])
    
# U ************************************************
# U ************************************************
# U ************************************************
 
    @classmethod
    def update_one(cls, **data):
        query = 'UPDATE users SET first_name=%(first_name)s WHERE id=%(id)s'
        return connectToMySQL(DATABASE_SCHEMA).query_db(query,data)

# D ************************************************
# D ************************************************
# D ************************************************
 
    @classmethod
    def delete_one(cls, **data):
        query = 'DELETE FROM users WHERE id=%(id)s'
        connectToMySQL(DATABASE_SCHEMA).query_db(query,data)
        return id


# ******************************************* VALIDATIONS ********************************************
    @staticmethod
    def validate_users(**data):
        is_valid = True

        if len(data['first_name']) < 3: 
            is_valid = False
            flash('first_name name must be greater than 3 characters')
        
        return is_valid