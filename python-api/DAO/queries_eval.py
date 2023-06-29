get_evaluation_by_id = "SELECT * FROM evaluation WHERE id_evaluation=%(id_evaluation)s"
insert_evaluation = "INSERT INTO evaluation (titreEvaluation, dateEvaluation, coeffEval, coeffItem, noteEval, noteItem, id_formateur_FK) VALUES (%s, %s, %s, %s, %s, %s, %s)"
update_evaluation = "UPDATE evaluation SET titreEvaluation=%s, dateEvaluation=%s WHERE id_evaluation=%s"
delete_evaluation = "DELETE FROM evaluation WHERE id_evaluation=%s"
get_all_evaluations ="SELECT * FROM evaluation"


# create_evaluation = """
# INSERT INTO evaluation (titreEvaluation, dateEvaluation, coeffEval, coeffItem, noteEval, noteItem, id_formateur_FK)
# VALUES (%s, %s, %s, %s, %s, %s, %s);

# SET @evaluation_id = LAST_INSERT_ID();

# INSERT INTO evaluation_item (id_evaluation_FK, id_item_FK)
# SELECT @evaluation_id, i.id_item
# FROM item AS i
# WHERE i.id_item IN (%s);
# """
