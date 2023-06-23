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

get_activite_by_formation = "SELECT * FROM activite WHERE id_formation_FK = %(id)s"
get_cp_by_activite = "SELECT * FROM cp WHERE id_activite_FK = %(id)s"
get_module_by_cp = "SELECT * FROM module WHERE id_cp_FK = %(id)s"
get_item_by_module = "SELECT * FROM item WHERE id_module_FK = %(id)s"

get_table_by_title = "SELECT 'formation' as bloc FROM formation WHERE titreFormation = %(title)s UNION SELECT 'activite' as bloc FROM activite WHERE titreActivite = %(title)s UNION SELECT 'cp' as bloc FROM cp WHERE titreCp = %(title)s UNION SELECT 'module' as bloc FROM module WHERE titreModule = %(title)s UNION SELECT 'item' as bloc FROM item WHERE titreItem = %(title)s;"

get_formation_by_title = "SELECT * FROM formation WHERE title = %(title)s;"
get_activite_by_title = "SELECT * FROM activite WHERE title = %(title)s;"
get_cp_by_title = "SELECT * FROM cp WHERE title = %(title)s;"
get_module_by_title = "SELECT * FROM module WHERE title = %(title)s;"
get_item_by_title = "SELECT * FROM item WHERE title = %(title)s;"