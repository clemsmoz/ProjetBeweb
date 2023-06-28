from flask import request, session
from DAO.connectionbdd import connection_params
from models.Administrateur import Administrateur
from models.Apprenant import Apprenant
from models.Formateur import Formateur
from models.Salarie import Salarie
import DAO.queries_general
import DAO.queries_admin
import DAO.queries_apprenant
import DAO.queries_formateur
import DAO.queries_salarie
import mysql.connector
import bcrypt
import jwt

def get_role(pseudo):
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            # Récupère le rôle de l'utilisateur en fonction de son pseudo
            c.execute(DAO.queries_general.select_table, {'pseudo': pseudo})
            result = c.fetchone()
            role = result[0]
            return role

def get_object(pseudo):
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            role = get_role(pseudo)
            if role == 'administrateur':
                # Récupère les données de l'administrateur correspondant au pseudo
                c.execute(DAO.queries_admin.get_admin, {'pseudo': pseudo})
                table = c.fetchall()
                user = []
                for row in table:
                    user = Administrateur(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    return user
            elif role == 'formateur':
                # Récupère les données du formateur correspondant au pseudo
                c.execute(DAO.queries_formateur.get_formateur, {'pseudo': pseudo})
                table = c.fetchall()
                user = []
                for row in table:
                    user = Formateur(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    return user
            elif role == 'apprenant':
                # Récupère les données de l'apprenant correspondant au pseudo
                c.execute(DAO.queries_apprenant.get_apprenant, {'pseudo': pseudo})
                table = c.fetchall()
                user = []
                for row in table:
                    user = Apprenant(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                    return user
            elif role == 'salarie':
                # Récupère les données du salarié correspondant au pseudo
                c.execute(DAO.queries_salarie.get_salarie, {'pseudo': pseudo})
                table = c.fetchall()
                user = []
                for row in table:
                    user = Salarie(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    return user
            else:
                return 'Rôle utilisateur non disponible.'

def verifyLog():
    if request.method == 'GET':
        pseudo = request.args.get('pseudo')
        password = request.args.get('password')

        with mysql.connector.connect(**connection_params) as db:
            with db.cursor() as c:
                # Vérifie si l'utilisateur existe et vérifie le mot de passe
                c.execute(DAO.queries_general.get_hashed_password, {'pseudo': pseudo})
                result = c.fetchone()

                if result is not None:
                    hashed_password = result[0]

                    if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                        user = get_object(pseudo)
                        # session['user'] = user
                        # Générer le token de connexion
                        c.execute(DAO.queries_general.select_infos, {'pseudo': pseudo})
                        table_result = c.fetchone()  
                        if table_result:
                            role, pseudo, section = table_result
                            # Générer le token de connexion en utilisant le nom de la table
                            payload = {'pseudo': pseudo, 'role': role, 'section': section}
                            secret_key = 'fondes2023'  # Remplacez par votre clé secrète
                            token = jwt.encode(payload, secret_key, algorithm='HS256')
                            session['token'] = token

                        return user
                    else:
                        return 'Mot de passe incorrect.'
                else:
                    return 'Utilisateur inconnu.'