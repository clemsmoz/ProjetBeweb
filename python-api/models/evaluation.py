import mysql.connector
import DAO.queries_eval

connection_params = {
    'host': "dbBB",
    'user': "user",
    'password': "password",
    'database': "db",
}

class Evaluation:
    def __init__(self, id_evaluation, titreEvaluation, dateEvaluation):
        self.id_evaluation = id_evaluation
        self.titre = titreEvaluation
        self.date_evaluation = dateEvaluation

def connect_to_database():
    return mysql.connector.connect(**connection_params)

def list_all_evaluations():
    with connect_to_database() as db:
        with db.cursor(dictionary=True) as cursor:
            cursor.execute(DAO.queries_eval.get_all_evaluations())
            return [Evaluation(**row) for row in cursor.fetchall()]

def get_evaluation(id_evaluation):
    with connect_to_database() as db:
        with db.cursor(dictionary=True) as cursor:
            cursor.execute(DAO.queries_eval.get_evaluation_by_id(), {'id_evaluation': id_evaluation})
            result = cursor.fetchone()
            if result:
                return Evaluation(**result)

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
