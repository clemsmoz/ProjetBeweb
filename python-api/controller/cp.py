from DAO.connectionbdd import connection_params
import mysql.connector
import DAO.queries_cp
from models.Cp import Cp

def connect_to_database():
    return mysql.connector.connect(**connection_params)


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
