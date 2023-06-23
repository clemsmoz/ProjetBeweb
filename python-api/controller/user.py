from flask import request
from DAO.connectionbdd import connection_params
import mysql.connector
import DAO.queries_admin
import DAO.queries_formateur
import DAO.queries_apprenant
import DAO.queries_salarie
from models.User import User
from models.Apprenant import Apprenant

def insertAdmin():
    if request.method == 'POST':
        prenom = request.form['firstName']
        nom = request.form['lastName']
        pseudo = request.form['pseudo']
        email = request.form['emailAddress']
        telephone = request.form['telephone']
        password = request.form['password']
        section = request.form['section']

        user = User(nom, prenom, pseudo, email, telephone, section)
        user.set_password(password)

        with mysql.connector.connect(**connection_params) as db:
            with db.cursor() as c:
                params = (user.nom, user.prenom, user.pseudo, user.email, user.telephone, user.get_password_hash(), user.section)
                params2 = (user.nom, user.prenom, user.pseudo+'-f', user.email, user.telephone, user.get_password_hash(), user.section)
                if request.form['formateur'] == 'y':
                    try:
                        c.execute(DAO.queries_formateur.insert_formateur, params2)
                        db.commit()
                        params = (user.nom, user.prenom)
                        c.execute(DAO.queries_formateur.get_formateur_id, params)
                        result = c.fetchone()
                        id_formateur = result[0]
                        params = (user.nom, user.prenom, user.pseudo, user.email, user.telephone, user.get_password_hash(), id_formateur, user.section)
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

        user = User(nom, prenom, pseudo, email, telephone, section)
        user.set_password(password)

        with mysql.connector.connect(**connection_params) as db:
            with db.cursor() as c:
                params = (user.nom, user.prenom, user.pseudo, user.email, user.telephone, user.get_password_hash(), user.section)
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

        apprenant = Apprenant(nom, prenom, pseudo, adresse, rib, secu, email, telephone, formation, section)
        apprenant.set_password(password)

        with mysql.connector.connect(**connection_params) as db:
            with db.cursor() as c:
                params = (apprenant.nom, apprenant.prenom, apprenant.pseudo, apprenant.adresse, apprenant.rib, apprenant.secu, apprenant.email, apprenant.telephone, apprenant.get_password_hash(), apprenant.formation, apprenant.section)
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

        user = User(nom, prenom, pseudo, email, telephone, section)
        user.set_password(password)

        with mysql.connector.connect(**connection_params) as db:
            with db.cursor() as c:
                params = (user.nom, user.prenom, user.pseudo, user.email, user.telephone, user.get_password_hash(), user.section)
                try:
                    c.execute(DAO.queries_salarie.insert_salarie, params)
                    db.commit()
                    return 'insertion réussie'
                except mysql.connector.Error as error:
                    print("Failed to execute query: {}".format(error))