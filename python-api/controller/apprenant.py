from DAO.connectionbdd import connection_params
import mysql.connector
import DAO.queries_apprenant
from models.Apprenant import Apprenant

def connect_to_database():
    return mysql.connector.connect(**connection_params)

def get_apprenant(pseudo):
    with connect_to_database() as db:
        with db.cursor() as c:
            c.execute(DAO.queries_apprenant.get_apprenant, {'pseudo':pseudo})
            result = c.fetchall()
            apprenant = []
            for row in result:
                apprenant = Apprenant(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11])
                return apprenant