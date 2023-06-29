from curses import window
from DAO.connectionbdd import connection_params
from flask import redirect, request, render_template, flash
import mysql.connector
import DAO.queries_eval
from models.Evaluation import Evaluation
import DAO.queries_activite
from models.Activite import Activite
import DAO.queries_cp
import DAO.queries_item
from models.Item import Item
import DAO.queries_module
import controller.activite
import controller.item
import json


def connect_to_database():
    return mysql.connector.connect(**connection_params)

def list_all_evaluations():
    with connect_to_database() as db:
        with db.cursor() as cursor:
            cursor.execute(DAO.queries_eval.get_all_evaluations)
            rows = cursor.fetchall()
            evaluations = []
            for row in rows:
                evaluation = Evaluation(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                evaluations.append(evaluation)
            return evaluations


def get_evaluation(id_evaluation):
    with connect_to_database() as db:
        with db.cursor() as c:
            c.execute(DAO.queries_eval.get_evaluation_by_id, {'id_evaluation': id_evaluation})
            result = c.fetchall()
            evaluation = []
            for row in result:
                evaluation = Evaluation(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            return evaluation

# def create_evaluation():
#     activites = controller.activite.get_all_activite()
#     if request.method == 'POST':
#         titreEvaluation = request.form['titreEvaluation']
#         dateEvaluation = request.form['dateEvaluation']
#         coeffItem = request.form['coeffItem']
#         coeffEval = request.form['coeffEval']
#         noteEval = request.form['noteEval']
#         noteItem = request.form['noteItem']
#         id_formation_FK = request.form['id_formation_FK']
#         id_item_FK = request.form.getlist('items')

#         with connect_to_database() as db:
#             with db.cursor() as cursor:
#                 insert_evaluation = """
#                 INSERT INTO evaluation (titreEvaluation, dateEvaluation, coeffEval, coeffItem, noteEval, noteItem, id_formateur_FK)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s)
#                 """
#                 params = (titreEvaluation, dateEvaluation, coeffEval, coeffItem, noteEval, noteItem, id_formation_FK)
#                 cursor.execute(insert_evaluation, params)
#                 db.commit()

#                 cursor.execute("SELECT LAST_INSERT_ID();")
#                 evaluation_id = cursor.fetchone()[0]

#                 insert_evaluation_item = """
#                 INSERT INTO evaluation_item (id_evaluation_FK, id_item_FK)
#                 SELECT %s, i.id_item
#                 FROM item AS i
#                 WHERE i.id_item IN (%s)
#                 """
#                 item_params = (evaluation_id, ','.join(id_item_FK))
#                 cursor.execute(insert_evaluation_item, item_params)
#                 db.commit()

#         flash('L\'évaluation a été créée avec succès.', 'success')
        
#     activites = controller.activite.get_all_activite()
#     return render_template('create_evaluations.html', activites=activites)
def create_evaluation():
    activites = controller.activite.get_all_activite()
    message = None  # Initialiser la variable message à None

    if request.method == 'POST':
        titreEvaluation = request.form['titreEvaluation']
        dateEvaluation = request.form['dateEvaluation']
        coeffItem = request.form['coeffItem']
        coeffEval = request.form['coeffEval']
        noteEval = request.form['noteEval']
        noteItem = request.form['noteItem']
        id_formation_FK = request.form['id_formation_FK']
        id_item_FK = request.form.get('items')
        id_item_FK = json.loads(id_item_FK)  # Convertir la chaîne JSON en liste d'entiers
        with connect_to_database() as db:
            with db.cursor() as cursor:
                insert_evaluation = "INSERT INTO evaluation (titreEvaluation, dateEvaluation, coeffEval, coeffItem, noteEval, noteItem, id_formateur_FK) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                params = (titreEvaluation, dateEvaluation, coeffEval, coeffItem, noteEval, noteItem, id_formation_FK)
                cursor.execute(insert_evaluation, params)
                db.commit()
                cursor.execute("SELECT LAST_INSERT_ID();")
                evaluation_id = cursor.fetchone()[0]
                insert_evaluation_item = "INSERT INTO evaluation_item (id_evaluation_FK, id_item_FK) VALUES (%s, %s)"
                for id_item in id_item_FK:
                    item_params = (evaluation_id, id_item)
                    cursor.execute(insert_evaluation_item, item_params)
                db.commit()
        message = 'L\'évaluation a été créée avec succès.'  # Définir le message de succès
    return render_template('create_evaluations.html', activites=activites, message=message)



def update_evaluation(id_evaluation, titreEvaluation, dateEvaluation):
    params = {'id_evaluation': id_evaluation, 'titre': titreEvaluation, 'date_evaluation': dateEvaluation}
    with connect_to_database() as db:
        with db.cursor() as cursor:
            cursor.execute(DAO.queries_eval.update_evaluation, params)
            db.commit()


def delete_evaluation(id_evaluation):
    with connect_to_database() as db:
        with db.cursor() as cursor:
            cursor.execute(DAO.queries_eval.delete_evaluation, {'id_evaluation': id_evaluation})
            db.commit()
