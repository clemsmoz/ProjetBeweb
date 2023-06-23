get_cp = "SELECT * FROM cp"

insert_cp = "INSERT INTO cp (id_Cp, titrecp, contenuCp, id_activite_FK) values (%s, %s, %s, %s)"

updade_cp = "UPDATE FROM cp SET id_cp = %s, titreCp = %s, contenuCp = %s, id_activite_FK = %s WHERE id_cp = %s"

delete_cp = "DELETE FROM cp WHERE id_cp = %s"
