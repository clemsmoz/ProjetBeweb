get_hashed_password = "SELECT password FROM (SELECT passwordAdmin AS password FROM administrateur WHERE pseudoAdmin = %(pseudo)s UNION ALL SELECT passwordSalarie AS password FROM salarie WHERE pseudoSalarie = %(pseudo)s UNION ALL SELECT passwordApprenant AS password FROM apprenant WHERE pseudoApprenant = %(pseudo)s UNION ALL SELECT passwordFormateur AS password FROM formateur WHERE pseudoFormateur = %(pseudo)s) AS passwords LIMIT 1"

get_user = "SELECT nomAdmin, prenomAdmin, pseudoAdmin, telephoneAdmin, emailAdmin, passwordAdmin, id_section_FK FROM administrateur WHERE pseudoAdmin = %(pseudo)s UNION SELECT nomFormateur, prenomFormateur, pseudoFormateur, telephoneFormateur, emailFormateur, passwordFormateur, id_section_FK FROM formateur WHERE pseudoFormateur = %(pseudo)s UNION SELECT nomApprenant, prenomApprenant, pseudoApprenant, telephoneApprenant, emailApprenant, passwordApprenant, id_section_FK FROM apprenant WHERE pseudoApprenant = %(pseudo)s UNION SELECT nomSalarie, prenomSalarie, pseudoSalarie, telephoneSalarie, emailSalarie, passwordSalarie, id_section_FK FROM salarie WHERE pseudoSalarie = %(pseudo)s;"

get_user_firstname = "SELECT CASE WHEN EXISTS (SELECT prenomAdmin FROM administrateur WHERE pseudoAdmin = %(pseudo)s) THEN (SELECT prenomAdmin FROM administrateur WHERE pseudoAdmin = %(pseudo)s) WHEN EXISTS (SELECT prenomSalarie FROM salarie WHERE pseudoSalarie = %(pseudo)s) THEN (SELECT prenomSalarie FROM salarie WHERE pseudoSalarie = %(pseudo)s) WHEN EXISTS (SELECT prenomApprenant FROM apprenant WHERE pseudoApprenant = %(pseudo)s) THEN (SELECT prenomApprenant FROM apprenant WHERE pseudoApprenant = %(pseudo)s) WHEN EXISTS (SELECT prenomFormateur FROM formateur WHERE pseudoFormateur = %(pseudo)s) THEN (SELECT prenomFormateur FROM formateur WHERE pseudoFormateur = %(pseudo)s) ELSE NULL END AS prenom_utilisateur;"

select_table = "SELECT 'administrateur' AS role FROM administrateur WHERE pseudoAdmin = %(pseudo)s UNION ALL SELECT 'salarie' AS table_name FROM salarie WHERE pseudoSalarie = %(pseudo)s UNION ALL SELECT 'apprenant' AS table_name FROM apprenant WHERE pseudoApprenant = %(pseudo)s UNION ALL SELECT 'formateur' AS table_name FROM formateur WHERE pseudoFormateur = %(pseudo)s;"

select_infos = "SELECT 'administrateur' AS role, pseudoAdmin AS pseudo, id_section_FK AS section FROM administrateur WHERE pseudoAdmin = %(pseudo)s UNION ALL SELECT 'salarie' AS role, pseudoSalarie AS pseudo, id_section_FK AS section FROM salarie WHERE pseudoSalarie = %(pseudo)s UNION ALL SELECT 'apprenant' AS role, pseudoApprenant AS pseudo, id_section_FK AS section FROM apprenant WHERE pseudoApprenant = %(pseudo)s UNION ALL SELECT 'formateur' AS role, pseudoFormateur AS pseudo, id_section_FK AS section FROM formateur WHERE pseudoFormateur = %(pseudo)s;"

select_table = "SELECT 'administrateur' AS role FROM administrateur WHERE pseudoAdmin = %(pseudo)s UNION ALL SELECT 'salarie' AS table_name FROM salarie WHERE pseudoSalarie = %(pseudo)s UNION ALL SELECT 'apprenant' AS table_name FROM apprenant WHERE pseudoApprenant = %(pseudo)s UNION ALL SELECT 'formateur' AS table_name FROM formateur WHERE pseudoFormateur = %(pseudo)s;"



update_password_admin = "UPDATE administrateur SET passwordAdmin = %(hashed_password)s WHERE pseudoAdmin = %(pseudo)s;"
update_password_formateur = "UPDATE formateur SET passwordFormateur = %(hashed_password)s WHERE pseudoFormateur = %(pseudo)s;"
update_password_salarie = "UPDATE salarie SET passwordSalarie = %(hashed_password)s WHERE pseudoSalarie = %(pseudo)s;"
update_password_apprenant = "UPDATE apprenant SET passwordApprenant = %(hashed_password)s WHERE pseudoApprenant = %(pseudo)s;"



