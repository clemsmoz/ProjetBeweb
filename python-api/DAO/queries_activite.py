get_activite = "SELECT * FROM activite"

insert_activite = "INSERT INTO activite (id_activite, titreActivite, resumeActivite, id_formation_FK) values (%s, %s, %s, %s)"

updade_activite = "UPDATE FROM activite SET id_activite = %s, titreActivite = %s, resumeActivite = %s, id_formation_FK = %s WHERE id_activite = %s"

delete_activite = "DELETE FROM activite WHERE id_activite = %s"

get_activite_by_apprenant = "SELECT DISTINCT activite.id_activite, activite.titreActivite, activite.resumeActivite, activite.id_formation_FK FROM `activite` INNER JOIN formation ON activite.id_formation_FK = formation.id_formation INNER JOIN apprenant ON formation.id_formation = apprenant.id_formation_FK WHERE apprenant.id_formation_FK = %s;"
