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

def get_bloc_by_title(title):
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            c.execute(DAO.queries_formation.get_table_by_title, {'title': title})
            result = c.fetchone()
            bloc = result[0]
            return bloc

def get_object_bloc(title):
    bloc = get_bloc_by_title(title)
    with mysql.connector.connect(**connection_params) as db:
        with db.cursor() as c:
            if bloc == 'formation':
                c.execute(DAO.queries_formation.get_formation_by_title, {'title': title})
                row = c.fetchone()
                if row:
                    objectBloc =  Formation(row[0], row[1], row[2])
                    return objectBloc
            elif bloc == 'activite':
                c.execute(DAO.queries_formation.get_activite_by_title, {'title': title})
                row = c.fetchone()
                if row:
                    objectBloc =  Activite(row[0], row[1], row[2], row[3])
                    return objectBloc
            elif bloc == 'cp':
                c.execute(DAO.queries_formation.get_cp_by_title, {'title': title})
                row = c.fetchone()
                if row:
                    objectBloc =  Cp(row[0], row[1], row[2], row[3])
                    return objectBloc
            elif bloc == 'module':
                c.execute(DAO.queries_formation.get_module_by_title, {'title': title})
                row = c.fetchone()
                if row:
                    objectBloc =  Module(row[0], row[1], row[2], row[3])
                    return objectBloc
            elif bloc == 'item':
                c.execute(DAO.queries_formation.get_item_by_title, {'title': title})
                row = c.fetchone()
                if row:
                    objectBloc =  Item(row[0], row[1], row[2], row[3])
                    return objectBloc
            return None
            
def select_bloc():
     if request.method == 'GET':
        title = request.args.get('form_title')
        bloc = get_bloc_by_title(title)
        objBloc = get_object_bloc(title)
        return bloc, objBloc