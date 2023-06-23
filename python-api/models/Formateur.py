<<<<<<< HEAD
from models.User import User

class Formateur(User):
    def __init__(self, id, nom, prenom, pseudo, email, telephone, password_hash, formation, section):
        super().__init__(id, nom, prenom, pseudo, email, telephone, password_hash, section)
        self.formation = formation
        
=======
from models.User import User

class Formateur(User):
    def __init__(self, id, nom, prenom, pseudo, email, telephone, password_hash, formation, section):
        super().__init__(id, nom, prenom, pseudo, email, telephone, password_hash, section)
        self.formation = formation
>>>>>>> 706f18afd9c9d68616a44f9f73cec89ac68481aa
