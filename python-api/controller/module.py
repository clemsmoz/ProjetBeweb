from DAO.connectionbdd import connection_params
import mysql.connector
import DAO.queries_module
from models.Module import Module

def connect_to_database():
    return mysql.connector.connect(**connection_params)


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
