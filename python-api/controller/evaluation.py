from DAO.connectionbdd import connection_params
import mysql.connector
import DAO.queries_eval
from models.Evaluation import Evaluation

def connect_to_database():
    return mysql.connector.connect(**connection_params)

def list_all_evaluations():
    with connect_to_database() as db:
        with db.cursor() as c:
            c.execute(DAO.queries_eval.get_all_evaluations)
            rows = c.fetchall()
            evaluations = []
            for row in rows:
                evaluation = Evaluation(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                )
                evaluations.append(evaluation)
            return evaluations


def get_evaluation(id_evaluation):
    with connect_to_database() as db:
        with db.cursor() as c:
            c.execute(DAO.queries_eval.get_evaluation_by_id, {'id_evaluation': id_evaluation})
            result = c.fetchall()
            evaluation = []
            for row in result:
                evaluation = Evaluation(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                return evaluation

def create_evaluation(titreEvaluation, dateEvaluation):
    params = {'titre': titreEvaluation, 'date_evaluation': dateEvaluation}
    with connect_to_database() as db:
        with db.cursor() as cursor:
            cursor.execute(DAO.queries_eval.insert_evaluation(), params)
            db.commit()

def update_evaluation(id_evaluation, titreEvaluation, dateEvaluation):
    params = {'id_evaluation': id_evaluation, 'titre': titreEvaluation, 'date_evaluation': dateEvaluation}
    with connect_to_database() as db:
        with db.cursor() as cursor:
            cursor.execute(DAO.queries_eval.update_evaluation(), params)
            db.commit()

def delete_evaluation(id_evaluation):
    with connect_to_database() as db:
        with db.cursor() as cursor:
            cursor.execute(DAO.queries_eval.delete_evaluation(), {'id_evaluation': id_evaluation})
            db.commit()