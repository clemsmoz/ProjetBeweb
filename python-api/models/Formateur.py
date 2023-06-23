from models.User import User

class Formateur(User):
    def __init__(self, id, nom, prenom, pseudo, email, telephone, password_hash, formation, section):
        super().__init__(id, nom, prenom, pseudo, email, telephone, password_hash, section)
        self.formation = formation
        
