from models.User import User

class Salarie(User):
    def __init__(self, id, nom, prenom, pseudo, email, telephone, password_hash, eval, section):
        super().__init__(id, nom, prenom, pseudo, email, telephone, password_hash, section)
        self.eval = eval

