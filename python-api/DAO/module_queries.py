get_module = "SELECT * FROM module"

insert_module = "INSERT INTO module (id_module, titreModule, contenuModule, id_cp_FK) values (%s, %s, %s, %s)"

updade_module = "UPDATE FROM module SET id_module = %s, titreModule = %s, contenuModule = %s, id_cp_FK = %s WHERE id_module = %s"

delete_module = "DELETE FROM module WHERE id_module = %s"
