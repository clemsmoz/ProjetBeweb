
get_apprenant = "SELECT * FROM apprenant WHERE pseudoApprenant = %(pseudo)s;"

get_apprenant = "SELECT * FROM apprenant WHERE pseudoApprenant = %(pseudo)s;"

insert_apprenant = "INSERT INTO apprenant (nomApprenant, prenomApprenant, pseudoApprenant, adresseApprenant, ribApprenant, secuApprenant, emailApprenant, telephoneApprenant, passwordApprenant, id_formation_FK, id_section_FK) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"