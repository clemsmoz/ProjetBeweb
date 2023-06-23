get_evaluation_by_id = "SELECT id_evaluation, titreEvaluation, dateEvaluation FROM evaluation WHERE id_evaluation=%s"
insert_evaluation = "INSERT INTO evaluation (titreEvaluation, dateEvaluation) VALUES (%s, %s)"
update_evaluation = "UPDATE evaluation SET titreEvaluation=%s, dateEvaluation=%s WHERE id_evaluation=%s"
delete_evaluation = "DELETE FROM evaluation WHERE id_evaluation=%s"
def get_all_evaluations():
    query = "SELECT id_evaluation, titreEvaluation, dateEvaluation FROM evaluation"
    # Code pour exécuter la requête SQL et obtenir les résultats
    # Stocker les résultats dans une liste d'objets
    evaluations = [
        {'id_evaluation': 1, 'titreEvaluation': 'Évaluation 1', 'dateEvaluation': '2023-06-22'},
        {'id_evaluation': 2, 'titreEvaluation': 'Évaluation 2', 'dateEvaluation': '2023-06-23'},
        {'id_evaluation': 3, 'titreEvaluation': 'Évaluation 3', 'dateEvaluation': '2023-06-24'}
    ]
    return evaluations