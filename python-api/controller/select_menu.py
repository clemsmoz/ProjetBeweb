from flask import request
from DAO.connectionbdd import connection_params
import mysql.connector
import models
import DAO.queries_admin
import DAO.queries_formateur
import DAO.queries_apprenant
import DAO.queries_salarie
import DAO.queries_formation   

def get_bloc_by_title(title):
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(DAO.queries_formation.get_table_by_title, {'title': title})
            result = c.fetchone()
            bloc = result[0]
            return bloc

def get_objetc_bloc(title):
    bloc = get_bloc_by_title(title)
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            if bloc == 'formation':
                c.execute(DAO.queries_formation.get_formation_by_title, {'title': title})
                table = c.fetchall()
                objectBloc = []
                for row in table:
                    objectBloc =  models.Formation.Formation(row[0], row[1], row[2])
                    return objectBloc
            elif bloc == 'activite':
                c.execute(DAO.queries_formation.get_activite_by_title, {'title': title})
                table = c.fetchall()
                objectBloc = []
                for row in table:
                    objectBloc =  models.Activite.Activite(row[0], row[1], row[2])
                    return objectBloc
            elif bloc == 'cp':
                c.execute(DAO.queries_formation.get_cp_by_title, {'title': title})
                table = c.fetchall()
                objectBloc = []
                for row in table:
                    objectBloc =  models.Cp.Cp(row[0], row[1], row[2])
                    return objectBloc
            elif bloc == 'module':
                c.execute(DAO.queries_formation.get_module_by_title, {'title': title})
                table = c.fetchall()
                objectBloc = []
                for row in table:
                    objectBloc =  models.Module.Module(row[0], row[1], row[2])
                    return objectBloc
            elif bloc == 'item':
                c.execute(DAO.queries_formation.get_item_by_title, {'title': title})
                table = c.fetchall()
                objectBloc = []
                for row in table:
                    objectBloc =  models.Item.Item(row[0], row[1], row[2])
                    return objectBloc
            else:
                return "Ce titre n'existe pas."
            
def select_bloc():
     if request.method == 'GET':
        title = request.args.get('form_title')