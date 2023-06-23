from flask import request
import bcrypt
from DAO.connectionbdd import connection_params
import mysql.connector
import DAO.queries_admin
import DAO.queries_formateur
import DAO.queries_apprenant
import DAO.queries_salarie

def insertAdmin():
    if request.method == 'POST':
        prenom = request.form['firstName']
        nom = request.form['lastName']
        pseudo = request.form['pseudo']
        email = request.form['emailAddress']
        telephone = request.form['telephone']
        password = request.form['password']
        section = request.form['section']

        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        with mysql.connector.connect(**connection_params) as db:
            with db.cursor() as c:
                params = (nom, prenom, pseudo, email, telephone, password_hash, section)
                params2 = (nom, prenom, pseudo+'-f', email, telephone, password_hash, section)
                if request.form['formateur'] == 'y':
                    try:
                        c.execute(DAO.queries_formateur.insert_formateur, params2)
                        db.commit()
                        params = (nom, prenom)
                        c.execute(DAO.queries_formateur.get_formateur_id, params)
                        result = c.fetchone()
                        id_formateur = result[0]
                        params = (nom, prenom, pseudo, email, telephone, password_hash, id_formateur, section)
                        c.execute(DAO.queries_admin.insert_admin_formateur_true, params)
                        db.commit()
                        return 'Insertion réussie'
                    except mysql.connector.Error as error:
                        print("Failed to execute query: {}".format(error))
                else:
                    try:
                        c.execute(DAO.queries_admin.insert_admin_formateur_false, params)
                        db.commit()
                        return 'Insertion réussie'
                    except mysql.connector.Error as error:
                        print("Failed to execute query: {}".format(error))

def insertFormateur():
    if request.method == 'POST':
        prenom = request.form['firstName']
        nom = request.form['lastName']
        pseudo = request.form['pseudo']
        email = request.form['emailAddress']
        telephone = request.form['telephone']
        password = request.form['password']
        section = request.form['section']

        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        with mysql.connector.connect(**connection_params) as db:
            with db.cursor() as c:
                params = (nom, prenom, pseudo, email, telephone, password_hash, section)
                try:
                    c.execute(DAO.queries_formateur.insert_formateur, params)
                    db.commit()
                    return 'insertion réussie'
                except mysql.connector.Error as error:
                    print("Failed to execute query: {}".format(error))

def insertApprenant():
    if request.method == 'POST':
        prenom = request.form['firstName']
        nom = request.form['lastName']
        pseudo = request.form['pseudo']
        adresse = request.form['adresse']
        rib = request.form['rib']
        secu = request.form['secu']
        email = request.form['emailAddress']
        telephone = request.form['telephone']
        password = request.form['password']
        formation = request.form['formation']
        section = request.form['section']

        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        with mysql.connector.connect(**connection_params) as db:
            with db.cursor() as c:
                params = (nom, prenom, pseudo, adresse, rib, secu, email, telephone, password_hash, formation, section)
                try:
                    c.execute(DAO.queries_apprenant.insert_apprenant, params)
                    db.commit()
                    return 'insertion réussie'
                except mysql.connector.Error as error:
                    print("Failed to execute query: {}".format(error))

def insertSalarie():
    if request.method == 'POST':
        prenom = request.form['firstName']
        nom = request.form['lastName']
        pseudo = request.form['pseudo']
        email = request.form['emailAddress']
        telephone = request.form['telephone']
        password = request.form['password']
        section = request.form['section']

        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        with mysql.connector.connect(**connection_params) as db:
            with db.cursor() as c:
                params = (nom, prenom, pseudo, email, telephone, password_hash, section)
                try:
                    c.execute(DAO.queries_salarie.insert_salarie, params)
                    db.commit()
                    return 'insertion réussie'
                except mysql.connector.Error as error:
                    print("Failed to execute query: {}".format(error))