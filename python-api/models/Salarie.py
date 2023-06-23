<<<<<<< HEAD
from models.User import User

class Salarie(User):
    def __init__(self, id, nom, prenom, pseudo, email, telephone, password_hash, eval, section):
        super().__init__(id, nom, prenom, pseudo, email, telephone, password_hash, section)
        self.eval = eval

=======
from models.User import User

class Salarie(User):
    def __init__(self, id, nom, prenom, pseudo, email, telephone, password_hash, eval, section):
        super().__init__(id, nom, prenom, pseudo, email, telephone, password_hash, section)
        self.eval = eval

>>>>>>> 706f18afd9c9d68616a44f9f73cec89ac68481aa
