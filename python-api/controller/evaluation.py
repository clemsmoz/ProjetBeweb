from curses import window
from DAO.connectionbdd import connection_params
from flask import request, render_template
import mysql.connector
import DAO.queries_eval
from models.Evaluation import Evaluation
import DAO.queries_activite
from models.Activite import Activite
from models.Cp import Cp
import DAO.queries_cp
import DAO.queries_item
from models.Item import Item
import DAO.queries_module
from models.Module import Module
import controller.activite
import controller.cp
import controller.item
import controller.module


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
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12]
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
                evaluation = Evaluation(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12]
                )
                return evaluation


def create_evaluation():
    activites = controller.activite.get_all_activite()
    if request.method == 'POST':
        titreEvaluation = request.form['titreEvaluation']
        dateEvaluation = request.form['dateEvaluation']
        coeffItem = request.form['coeffItem']
        coeffEval = request.form['coeffEval']
        noteEval = request.form['noteEval']
        noteItem = request.form['noteItem']
        id_activite_FK = request.form['activites']
        id_cp_FK = request.form['cps']
        id_item_FK = request.form['items']
        id_module_FK = request.form['modules']
        params = {
            'titreEvaluation': titreEvaluation,
            'dateEvaluation': dateEvaluation,
            'coeffItem': coeffItem,
            'coeffEval': coeffEval,
            'noteEval': noteEval,
            'noteItem': noteItem,
            'id_activite_FK': id_activite_FK,
            'id_cp_FK': id_cp_FK,
            'id_module_FK': id_module_FK,
            'id_item_FK': id_item_FK
        }

        with connect_to_database() as db:
            with db.cursor() as cursor:
                cursor.execute(DAO.queries_eval.insert_evaluation(), params)
                db.commit()

        return "window.location.href='/evaluations'"
    else:
        Cps = controller.cp.get_all_cps()
        items = controller.item.get_all_items()
        modules = controller.module.get_all_modules()
        return render_template('create_evaluations.html', activites=activites, Cps=Cps, items=items, modules=modules)


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
