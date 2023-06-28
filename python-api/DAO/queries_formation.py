##################################### SELECT ##############################################

get_all_formations = "SELECT * FROM formation"
get_all_activites = "SELECT* FROM activite"
get_all_cp = "SELECT * FROM cp"
get_all_modules = "SELECT * FROM module"
get_all_items = "SELECT * FROM item"

get_formation_by_id = "SELECT * FROM formation WHERE id_formation = %(id)s"
get_activite_by_id = "SELECT * FROM activite WHERE id_activite = %(id)s"
get_cp_by_id = "SELECT * FROM cp WHERE id_cp = %(id)s"
get_module_by_id = "SELECT * FROM module WHERE id_module = %(id)s"
get_item_by_id = "SELECT * FROM item WHERE id_item = %(id)s"

get_table_by_title = "SELECT 'formation' as bloc FROM formation WHERE titreFormation = %(title)s UNION SELECT 'activite' as bloc FROM activite WHERE titreActivite = %(title)s UNION SELECT 'cp' as bloc FROM cp WHERE titreCp = %(title)s UNION SELECT 'module' as bloc FROM module WHERE titreModule = %(title)s UNION SELECT 'item' as bloc FROM item WHERE titreItem = %(title)s;"

get_table_by_id = "SELECT 'formation' as bloc FROM formation WHERE id_formation = %(id)s UNION SELECT 'activite' as bloc FROM activite WHERE id_activite = %(id)s UNION SELECT 'cp' as bloc FROM cp WHERE id_cp = %(id)s UNION SELECT 'module' as bloc FROM module WHERE  id_module = %(id)s UNION SELECT 'item' as bloc FROM item WHERE id_item = %(id)s;"

get_formation_by_title = "SELECT * FROM formation WHERE titreFormation = %(title)s;"
get_activite_by_title = "SELECT * FROM activite WHERE titreActivite = %(title)s;"
get_cp_by_title = "SELECT * FROM cp WHERE titreCp = %(title)s;"
get_module_by_title = "SELECT * FROM module WHERE titreModule = %(title)s;"
get_item_by_title = "SELECT * FROM item WHERE titreItem = %(title)s;"

get_id_formation = "SELECT id_formation FROM formation WHERE titreFormation = %(title)s"
get_activites_by_formation = "SELECT * FROM activite WHERE id_formation_FK = %(id)s"
get_cp_by_activite = "SELECT * FROM cp WHERE id_activite_FK = %(id)s"
get_module_by_cp = "SELECT * FROM module WHERE id_cp_FK = %(id)s"
get_item_by_module = "SELECT * FROM item WHERE id_module_FK = %(id)s"
get_cps_by_formation = "SELECT cp.* FROM activite INNER JOIN cp ON activite.id_activite = cp.id_activite_FK WHERE activite.id_formation_FK = %(id)s"

get_modules_by_formation = "SELECT module.* FROM cp INNER JOIN "

##################################### DELETE ##############################################

delete_activite_by_FK = "DELETE FROM activite WHERE id_formation_FK = %(id)s;"
delete_cp_by_FK = "DELETE FROM cp WHERE id_activite_FK = %(id)s;"
delete_module_by_FK = "DELETE FROM module WHERE id_cp_FK = %(id)s;"
delete_item_by_FK  = "DELETE FROM item WHERE id_module_FK= %(id)s"


delete_formation_by_id = "DELETE FROM formation WHERE id_formation = %(id)s;"
delete_activites_by_formation = "DELETE FROM activite WHERE id_formation_FK = %(id)s;"
delete_cps_by_formation = "DELETE cp FROM activite INNER JOIN cp ON activite.id_activite = cp.id_activite_FK WHERE activite.id_formation_FK = %(id)s"
delete_modules_by_formation = "DELETE module FROM activite INNER JOIN cp ON activite.id_activite = cp.id_activite_FK INNER JOIN module ON cp.id_cp = module.id_cp_FK WHERE activite.id_formation_FK = %(id)s"
delete_items_by_formation = "DELETE item FROM activite INNER JOIN cp ON activite.id_activite = cp.id_activite_FK INNER JOIN module ON cp.id_cp = module.id_cp_FK INNER JOIN item ON module.id_module = item.id_module_FK WHERE activite.id_formation_FK = %(id)s"


delete_activite_by_id = "DELETE FROM activite WHERE id_activite = %(id)s;"
delete_cps_by_activite = "DELETE FROM cp WHERE id_activite_FK = %(id)s;"
delete_modules_by_activite = "DELETE module FROM module INNER JOIN cp ON module.id_cp_FK = cp.id_cp INNER JOIN activite ON cp.id_activite_FK = activite.id_activite WHERE activite.id_activite = %(id)s"
delete_items_by_activite = "DELETE item FROM item INNER JOIN module ON item.id_module_FK = module.id_module INNER JOIN cp ON module.id_cp_FK = cp.id_cp INNER JOIN activite ON cp.id_activite_FK = activite.id_activite WHERE activite.id_activite = %(id)s"

delete_cp_by_id = "DELETE FROM cp WHERE id_cp = %(id)s;"
delete_modules_by_cp = "DELETE FROM module WHERE id_cp_FK = %(id)s"
delete_items_by_cp = "DELETE item FROM item INNER JOIN module ON item.id_module_FK = module.id_module INNER JOIN cp ON module.id_cp_FK = cp.id_cp WHERE cp.id_cp = %(id)s"

delete_module_by_id = "DELETE FROM module WHERE id_module = %(id)s;"
delete_items_by_module = "DELETE FROM item WHERE id_module_FK = %(id)s"

delete_item_by_id = "DELETE FROM item WHERE id_item = %(id)s;"


##################################### INSERT ##############################################

create_formation = "INSERT INTO formation (titreFormation, resumeFormation) values(%s, %s)"
create_activite = "INSERT INTO activite (titreActivite, resumeActivite, id_formation_FK) values (%s, %s, %s)"
create_cp = "INSERT INTO cp (titreCp, contenuCp, id_activite_FK) values (%s, %s, %s)"
create_module = "INSERT INTO module (titreModule, contenuModule, id_cp_FK) values (%s, %s, %s)"
create_item = "INSERT INTO item (titreItem, contenuItem, id_module_FK) values (%s, %s, %s)"

##################################### UPDATE ##############################################

update_formation = "UPDATE formation SET titreFormation = %s, resumeFormation = %s WHERE id_formation = %s"
update_activite = "UPDATE activite SET titreActivite = %s, resumeActivite = %s WHERE id_activite = %s"
update_cp = "UPDATE cp SET titreCp = %s, contenuCp = %s WHERE id_cp = %s"
update_module = "UPDATE module SET titreModule = %s, contenuModule = %s WHERE id_module = %s"
update_item = "UPDATE item SET titreItem = %s, contenuItem = %s WHERE id_item = %s"