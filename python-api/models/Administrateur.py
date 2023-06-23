<<<<<<< HEAD
from models.User import User

class Administrateur(User):
    def __init__(self, id, nom, prenom, pseudo, email, telephone, password_hash, formateur, section):
        super().__init__(id, nom, prenom, pseudo, email, telephone, password_hash, section)
        self.formateur = formateur

=======
from models.User import User

class Administrateur(User):
    def __init__(self, id, nom, prenom, pseudo, email, telephone, password_hash, formateur, section):
        super().__init__(id, nom, prenom, pseudo, email, telephone, password_hash, section)
        self.formateur = formateur

>>>>>>> 706f18afd9c9d68616a44f9f73cec89ac68481aa
