from models.User import User

class Administrateur(User):
    def __init__(self, id, nom, prenom, pseudo, email, telephone, password_hash, formateur, section):
        super().__init__(id, nom, prenom, pseudo, email, telephone, password_hash, section)
        self.formateur = formateur

