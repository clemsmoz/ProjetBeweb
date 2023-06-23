get_activite = "SELECT * FROM activite"

insert_activite = "INSERT INTO activite (id_activite, titreActivite, resumeActivite, id_formation_FK) values (%s, %s, %s, %s)"

updade_activite = "UPDATE FROM activite SET id_activite = %s, titreActivite = %s, resumeActivite = %s, id_formation_FK = %s WHERE id_activite = %s"

delete_activite = "DELETE FROM activite WHERE id_activite = %s"
