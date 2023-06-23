get_salarie = "SELECT * FROM salarie WHERE pseudoSalarie = %(pseudo)s;"

insert_salarie = "INSERT INTO salarie (nomSalarie, prenomSalarie, pseudoSalarie, emailSalarie, telephoneSalarie, passwordSalarie, id_section_FK) values (%s, %s, %s, %s, %s, %s, %s)"