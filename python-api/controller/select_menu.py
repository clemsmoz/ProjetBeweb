# importations des modules nécéssaires
from flask import request
from DAO.connectionbdd import connection_params
import mysql.connector
import DAO.queries_admin
import DAO.queries_formateur
import DAO.queries_apprenant
import DAO.queries_salarie
import DAO.queries_formation   
from models.Formation import Formation
from models.Activite import Activite
from models.Cp import Cp
from models.Module import Module
from models.Item import Item
import json


def list_formations():
    # Récupérer toutes les formations depuis la base de données
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(DAO.queries_formation.get_all_formations)
            rows = c.fetchall()
            formations = []
            for row in rows:
                # Créer des objets Formation à partir des résultats de la requête
                formation = Formation(
                    row[0], row[1], row[2]
                )
                formations.append(formation)
            return formations

def get_activites(id):
    # Récupérer toutes les activités pour une formation donnée
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(DAO.queries_formation.get_activites_by_formation, {'id': id})
            rows = c.fetchall()
            activites = []
            for row in rows:
                # Créer des objets Activite à partir des résultats de la requête
                activite = Activite(
                    row[0], row[1], row[2], row[3]
                )
                activites.append(activite)
            return activites

def get_cps(id):
    # Récupérer tous les cps pour une activité donnée
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(DAO.queries_formation.get_cp_by_activite, {'id': id})
            rows = c.fetchall()
            cps = []
            for row in rows:
                # Créer des objets cp à partir des résultats de la requête
                cp = Cp(
                    row[0], row[1], row[2], row[3]
                )
                cps.append(cp)
            return cps

def get_modules(id):
    # Récupérer tous les modules pour une compétence donnée
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(DAO.queries_formation.get_module_by_cp, {'id': id})
            rows = c.fetchall()
            modules = []
            for row in rows:
                # Créer des objets module à partir des résultats de la requête
                module = Module(
                    row[0], row[1], row[2], row[3]
                )
                modules.append(module)
            return modules

def get_items(id):
    # Récupérer tous les items pour un module donné
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(DAO.queries_formation.get_item_by_module, {'id': id})
            rows = c.fetchall()
            items = []
            for row in rows:
                # Créer des objets item à partir des résultats de la requête
                item = Item(
                    row[0], row[1], row[2], row[3]
                )
                items.append(item)
            return items


def get_bloc_by_title(title):
    # Récupérer un bloc (formation, activité, CP, module ou item) en fonction de son titre
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(DAO.queries_formation.get_table_by_title, {'title': title})
            result = c.fetchone()
            return result
        
def get_bloc_by_id(id):
    # Récupérer un bloc (formation, activité, CP, module ou item) en fonction de son id
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(DAO.queries_formation.get_table_by_id, {'id': id})
            result = c.fetchone()
            bloc = result[0]
            return bloc    

def get_object_bloc(title):
    # Récupérer un objet en fonction du bloc et du titre(formation, activité, CP, module ou item)
    bloc = get_bloc_by_title(title)
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            if bloc == 'formation':
                # requete pour recupérer une formation par son titre
                c.execute(DAO.queries_formation.get_formation_by_title, {'title': title})
                row = c.fetchone()
                if row:
                    #création d'un objet Formation avec les resultats
                    objectBloc =  Formation(row[0], row[1], row[2])
                    return objectBloc
            elif bloc == 'activite':
                # requete pour recupérer une activite par son titre
                c.execute(DAO.queries_formation.get_activite_by_title, {'title': title})
                row = c.fetchone()
                if row:
                    # création d'un objet Activite avec les resultats
                    objectBloc =  Activite(row[0], row[1], row[2], row[3])
                    return objectBloc
            elif bloc == 'cp':
                # requete pour recupérer une compétence par son titre
                c.execute(DAO.queries_formation.get_cp_by_title, {'title': title})
                row = c.fetchone()
                if row:
                    # création d'un objet Cp avec les resultats
                    objectBloc =  Cp(row[0], row[1], row[2], row[3])
                    return objectBloc
            elif bloc == 'module':
                # requete pour recupérer un module par son titre
                c.execute(DAO.queries_formation.get_module_by_title, {'title': title})
                row = c.fetchone()
                if row:
                    # création d'un objet Module avec les resultats
                    objectBloc =  Module(row[0], row[1], row[2], row[3])
                    return objectBloc
            elif bloc == 'item':
                # requete pour recupérer un item par son titre
                c.execute(DAO.queries_formation.get_item_by_title, {'title': title})
                row = c.fetchone()
                if row:
                    # création d'un objet Item avec les resultats
                    objectBloc =  Item(row[0], row[1], row[2], row[3])
                    return objectBloc
            return None

# Récupérer un objet en fonction du bloc et de l'id (formation, activité, CP, module ou item)
def get_object_bloc_by_id(id, table):
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            if table == 'formation':
                c.execute(DAO.queries_formation.get_formation_by_id, {'id': id})
                row = c.fetchone()
                if row:
                    objectBloc =  Formation(row[0], row[1], row[2])
                    return objectBloc
            elif table == 'activite':
                c.execute(DAO.queries_formation.get_activite_by_id, {'id': id})
                row = c.fetchone()
                if row:
                    objectBloc =  Activite(row[0], row[1], row[2], row[3])
                    return objectBloc
            elif table == 'cp':
                c.execute(DAO.queries_formation.get_cp_by_id, {'id': id})
                row = c.fetchone()
                if row:
                    objectBloc =  Cp(row[0], row[1], row[2], row[3])
                    return objectBloc
            elif table == 'module':
                c.execute(DAO.queries_formation.get_module_by_id, {'id': id})
                row = c.fetchone()
                if row:
                    objectBloc =  Module(row[0], row[1], row[2], row[3])
                    return objectBloc
            elif table == 'item':
                c.execute(DAO.queries_formation.get_item_by_id, {'id': id})
                row = c.fetchone()
                if row:
                    objectBloc =  Item(row[0], row[1], row[2], row[3])
                    return objectBloc
            return None

def get_list_obj(id, table):
    # Récupérer une liste d'objets (activités, CP, modules ou items) pour un bloc (formation, activité, CP ou module) donné
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            if table == 'formation':
                # Pour une formation donnée, récupérer toutes les activités
                objList = get_activites(id)
                return objList    
            elif table == 'activite':
                # Pour une activité donnée, récupérer tous les CP
                objList = get_cps(id)
                return objList
            elif table == 'cp':
                # Pour un CP donné, récupérer tous les modules
                objList = get_modules(id)
                return objList
            elif table == 'module':
                # Pour un module donné, récupérer tous les items
                objList = get_items(id)
                return objList
            return None
        
def select_bloc():
    if request.method == 'GET':
        title = request.args.get('form_title')
        objBloc = get_object_bloc(title)
        title = objBloc.get_titre()
        return title

def deletB(table, id):
    # Supprimer un bloc (formation, activité, CP, module ou item) en fonction de la table et de l'ID spécifiés
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            if table == 'formation':
                # Supprimer la formation et tous les éléments associés (activités, CP, modules et items)
                c.execute(DAO.queries_formation.delete_formation_by_id, {'id': id})
                db.commit()
                c.execute(DAO.queries_formation.delete_activites_by_formation, {'id': id})
                db.commit()
                c.execute(DAO.queries_formation.delete_cps_by_formation, {'id': id})
                db.commit()
                c.execute(DAO.queries_formation.delete_modules_by_formation, {'id': id})
                db.commit()
                c.execute(DAO.queries_formation.delete_items_by_formation, {'id': id})
                db.commit()
                return 'La formation a été supprimée'
            elif table == 'activite':
                # Supprimer l'activité et tous les éléments associés (CP, modules et items)
                c.execute(DAO.queries_formation.delete_activite_by_id, {'id': id})
                db.commit()
                c.execute(DAO.queries_formation.delete_cps_by_activite, {'id': id})
                db.commit()
                c.execute(DAO.queries_formation.delete_modules_by_activite, {'id': id})
                db.commit()
                c.execute(DAO.queries_formation.delete_items_by_activite, {'id': id})
                db.commit()
                return "L'activité a été supprimée"
            elif table == 'cp':
                # Supprimer le CP et tous les éléments associés (modules et items)
                c.execute(DAO.queries_formation.delete_cp_by_id, {'id': id})
                db.commit()
                c.execute(DAO.queries_formation.delete_modules_by_cp, {'id': id})
                db.commit()
                c.execute(DAO.queries_formation.delete_items_by_cp, {'id': id})
                db.commit()
                return "La compétence a été supprimée"
            elif table == 'module':
                # Supprimer le module et tous les items associés
                c.execute(DAO.queries_formation.delete_module_by_id, {'id': id})
                db.commit()
                c.execute(DAO.queries_formation.delete_items_by_module, {'id': id})
                db.commit()
                return "Le module a été supprimé"
            elif table == 'item':
                # Supprimer l'item
                c.execute(DAO.queries_formation.delete_item_by_id, {'id': id})
                db.commit()
                return "L'item a été supprimé"
            else:
                return "Une erreur est survenue lors de la suppression"
            
def update_obj(id, table):
    # mise a jour des données d'une table et des blocs (activité, cp, module, item) liés
    if request.method == 'POST':
        # recupération des inputs
        objBlocTitre = request.form['objBlocTitre']
        objBlocContenu = request.form['objBlocContenu']
        objIds = request.form.getlist('objIds[]')
        objTitres = request.form.getlist('objTitres[]')
        objContenus = request.form.getlist('objContenus[]')
        if objIds and objTitres and objContenus :
            objIds = json.loads(objIds[0])
            objTitres = json.loads(objTitres[0])
            objContenus = json.loads(objContenus[0])

        params = (objBlocTitre, objBlocContenu, id)
        with mysql.connector.connect(**connection_params) as db:
            try:
                with db.cursor() as c:
                    if table == 'formation':
                        # Maj de la formation
                        c.execute(DAO.queries_formation.update_formation, params)
                        db.commit()
                        # Maj des activités associées
                        for titre, contenu, objId in zip(objTitres, objContenus, objIds):
                            params2 = (titre, contenu, objId) 
                            c.execute(DAO.queries_formation.update_activite, params2)
                            db.commit()
                        return 'La formation a été modifiée'
                    elif table == 'activite':
                        # Maj de l'activite
                        c.execute(DAO.queries_formation.update_activite, params)
                        db.commit()
                        # Maj des cps associées
                        for titre, contenu, objId in zip(objTitres, objContenus, objIds):
                            params2 = (titre, contenu, objId)
                            c.execute(DAO.queries_formation.update_cp, params2)
                            db.commit()
                        return "l'activité a été modifiée"
                    elif table == 'cp':
                        # Maj de la compétence
                        c.execute(DAO.queries_formation.update_cp, params)
                        db.commit()
                        # Maj des modules associés
                        for titre, contenu, objId in zip(objTitres, objContenus, objIds):
                            params2 = (titre, contenu, objId)
                            c.execute(DAO.queries_formation.update_module, params2)
                            db.commit()
                        return "la compétence a été modifiée"
                    elif table == 'module':
                        # Maj du module
                        c.execute(DAO.queries_formation.update_module, params)
                        db.commit()
                        # Maj des items associés 
                        for titre, contenu, objId in zip(objTitres, objContenus, objIds):
                            params2 = (titre, contenu, objId)
                            c.execute(DAO.queries_formation.update_item, params2)
                            db.commit()
                        return "le module a été modifié"
                    elif table == 'item':
                        # Maj de l'item
                        c.execute(DAO.queries_formation.update_item, params)
                        db.commit()
                        return "l'item a été modifié"
            except Exception as e:
                return "une erreur est survenue lors de la mise a jour :"+str(e)