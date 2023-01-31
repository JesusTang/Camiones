from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Truck:
    db = 'example3'
    def __init__(self, data):
        self.id = data['id']
        self.patente = data['patente']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO camiones ( patente, user_id) VALUES (%(patente)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM camiones;"
        results =  connectToMySQL(cls.db).query_db(query)
        all_deseos = []
        for row in results:
            all_deseos.append( cls(row) )
        return all_deseos
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM camiones WHERE id = %(id)s;"
        result =connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])

    @classmethod
    def actualizar(cls, data):
        print(data, "DATA - "*1)
        flash("Correcta Actualización")
        query = "UPDATE camiones SET patente=%(patente)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM camiones WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    # @classmethod
    # def granted(cls,data):
    #     query = "DELETE FROM deseos WHERE id = %(id)s;"
    #     return connectToMySQL(cls.db).query_db(query,data)

    # class Post(db.Model):
    #     __searchable__= ["patente"]
    #     id =

    @staticmethod
    def validate_deseo(deseo):
        is_valid = True
        # if len(deseo['nd']) < 7:
        #     is_valid = False
        #     flash("Item name must be at least 3 characters","deseo")
        if len(deseo['patente']) < 3:
            is_valid = False
            flash("description must be at least 10 characters","deseo")
        return is_valid