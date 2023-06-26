get_formateur = "SELECT * FROM formateur WHERE pseudoFormateur = %(pseudo)s;"

insert_formateur = "INSERT INTO formateur (nomFormateur, prenomFormateur, pseudoFormateur, emailFormateur, telephoneFormateur, passwordFormateur, id_section_FK) values (%s, %s, %s, %s, %s, %s, %s)"

get_formateur_id = "SELECT id_formateur FROM formateur WHERE nomFormateur=%s AND prenomFormateur=%s"