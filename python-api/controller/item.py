from DAO.connectionbdd import connection_params
import mysql.connector
import DAO.queries_item
from models.Item import Item

def connect_to_database():
    return mysql.connector.connect(**connection_params)


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
