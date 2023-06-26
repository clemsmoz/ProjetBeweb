from DAO.connectionbdd import connection_params
import mysql.connector
import DAO.queries_activite
from models.Activite import Activite
from models.Cp import Cp
import DAO.queries_cp
import DAO.queries_item
from models.Item import Item
import DAO.queries_module
from models.Module import Module

def connect_to_database():
    return mysql.connector.connect(**connection_params)

def get_all_activite():
    with connect_to_database() as db:
        with db.cursor() as cursor:
            cursor.execute(DAO.queries_activite.get_activite)
            rows = cursor.fetchall()
            activites = []
            for row in rows:
                activite = Activite(
                    row[0], row[1], row[2], row[3]
                )
                activites.append(activite)
            
            Cps = get_all_cp()
            items = get_all_item()
            modules = get_all_module()
            
            return activites, Cps, items, modules
        
def get_all_cp():
    with connect_to_database() as db:
        with db.cursor() as cursor:
            cursor.execute(DAO.queries_cp.get_cp)
            rows = cursor.fetchall()
            Cps = []
            for row in rows:
                cp = Cp(
                    row[0],row[1],row[2], row[3])
                Cps.append(cp)
            return Cps
        
        
def get_all_item():
    with connect_to_database() as db:
        with db.cursor() as cursor:
            cursor.execute(DAO.queries_item.get_item)
            rows = cursor.fetchall()
            items = []
            for row in rows:
                item = Item(
                    row[0],row[1],row[2], row[3])
                items.append(item)
            return items

def get_all_module():
    with connect_to_database() as db:
        with db.cursor() as cursor:
            cursor.execute(DAO.queries_module.get_module)
            rows = cursor.fetchall()
            modules = []
            for row in rows:
                module = Module(
                    row[0],row[1],row[2], row[3])
                modules.append(module)
            return modules


