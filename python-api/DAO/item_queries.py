get_item = "SELECT * FROM item"

insert_item = "INSERT INTO item (id_item, titreItem, contenuItem, id_module_FK) values (%s, %s, %s, %s)"

updade_item = "UPDATE FROM item SET id_item = %s, titreItem = %s, contenuItem = %s, id_module_FK = %s WHERE id_item = %s"

delete_item = "DELETE FROM item WHERE id_item = %s"
