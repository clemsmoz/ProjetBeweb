from flask import request
from DAO.connectionbdd import connection_params
import mysql.connector
import bcrypt
import DAO.queries_general
import controller.login
def updateThisPassword(method):
    if method == 'POST':
        try:
            pseudo = request.form['pseudo']
            password = request.form['password']
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            params = {'pseudo': pseudo, 'hashed_password': hashed_password }

            role = controller.login.get_role(pseudo)
            
            if role:
                if role == 'administrateur':
                    update_password = DAO.queries_general.update_password_admin
                elif role == 'formateur':
                    update_password = DAO.queries_general.update_password_formateur
                elif role == 'salarie':
                    update_password = DAO.queries_general.update_password_salarie
                elif role == 'apprenant':
                    update_password = DAO.queries_general.update_password_apprenant
                else:
                    return 'table inconnue'
                with mysql.connector.connect(**connection_params) as db:
                    with db.cursor() as c:
                        c.execute(update_password, params)
                        db.commit()
                return 'Mot de passe mis à jour avec succès'
            else:
                return 'Pseudo introuvable dans toutes les tables.'

        except mysql.connector.Error as error:
            print("Failed to execute query: {}".format(error))

