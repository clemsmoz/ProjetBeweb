<<<<<<< HEAD
<<<<<<< HEAD
get_admin = "SELECT * FROM administrateur WHERE pseudoAdmin = %(pseudo)s;"

insert_admin_formateur_false = "INSERT INTO administrateur (nomAdmin, prenomAdmin, pseudoAdmin, emailAdmin, telephoneAdmin, passwordAdmin, id_section_FK) values (%s, %s, %s, %s, %s, %s, %s)"
=======
=======
get_admin = "SELECT * FROM administrateur WHERE pseudoAdmin = %(pseudo)s;"

>>>>>>> 706f18afd9c9d68616a44f9f73cec89ac68481aa
insert_admin_formateur_false = "INSERT INTO administrateur (nomAdmin, prenomAdmin, pseudoAdmin, emailAdmin, telephoneAdmin, passwordAdmin, id_section_FK) values (%s, %s, %s, %s, %s, %s, %s)"

insert_admin_formateur_true = "INSERT INTO administrateur (nomAdmin, prenomAdmin, pseudoAdmin, emailAdmin, telephoneAdmin, passwordAdmin, id_formateur_FK, id_section_FK) values (%s, %s, %s, %s, %s, %s, %s, %s)"
>>>>>>> origin/test

<<<<<<< HEAD
insert_admin_formateur_true = "INSERT INTO administrateur (nomAdmin, prenomAdmin, pseudoAdmin, emailAdmin, telephoneAdmin, passwordAdmin, id_formateur_FK, id_section_FK) values (%s, %s, %s, %s, %s, %s, %s, %s)"

=======
>>>>>>> 706f18afd9c9d68616a44f9f73cec89ac68481aa
select_admin_by_pseudo = "SELECT * FROM Administrateur WHERE pseudoAdmin = %s"
