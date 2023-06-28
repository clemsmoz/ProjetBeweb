from flask import request
from DAO.connectionbdd import connection_params
import mysql.connector
import DAO.queries_formation

def insertFormation():
    if request.method == 'POST':
        titreFormation = request.form['form_title']
        resumeFormation = request.form['form_content']
        titresActivites = request.form.getlist('act_title')
        resumesActivites = request.form.getlist('act_content')
        
        with mysql.connector.connect(**connection_params) as db:
            with db.cursor() as c:
                try:
                    params = (titreFormation, resumeFormation)
                    c.execute(DAO.queries_formation.create_formation, params)
                    db.commit()
                    
                    c.execute(DAO.queries_formation.get_id_formation, {'title': titreFormation})
                    id_formation = c.fetchone()[0]  # Récupérer l'id de la formation
                    
                    for titreActivite, resumeActivite in zip(titresActivites, resumesActivites):
                        params2 = (titreActivite, resumeActivite, id_formation)
                        c.execute(DAO.queries_formation.create_activite, params2)
                        db.commit()
                    return "Formation créé"
                except mysql.connector.Error as error:
                    print("Failed to execute query: {}".format(error))
