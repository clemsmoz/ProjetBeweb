from models.User import User

class Apprenant(User):
    def __init__(self, id, nom, prenom, pseudo, adresse, rib, secu, email, telephone, password_hash, formation, section):
        super().__init__(id, nom, prenom, pseudo, email, telephone, password_hash, section)
        self.adresse = adresse
        self.rib = rib
        self.secu = secu
        self.formation = formation

