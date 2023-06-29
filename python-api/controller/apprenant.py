import DAO.queries_apprenant 
from models.Apprenant import Apprenant
from DAO.connectionbdd import connection_params
import mysql.connector



def connect_to_database():
    return mysql.connector.connect(**connection_params)


def get_all_apprenants():
    with connect_to_database() as db:
        with db.cursor() as cursor:
            cursor.execute(DAO.queries_apprenant.get_all_apprenants)
            rows = cursor.fetchall()
            apprenants = []
            for row in rows:
                apprenant = Apprenant(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],row[8], row[9], row[10], row[11])
                apprenants.append(apprenant)
            return apprenants