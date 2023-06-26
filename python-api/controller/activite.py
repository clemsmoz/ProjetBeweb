from DAO.connectionbdd import connection_params
import mysql.connector
import DAO.queries_activite
from models.Activite import Activite

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
                    row[0],row[1],row[2], row[3])
                activites.append(activite)
            return activites
