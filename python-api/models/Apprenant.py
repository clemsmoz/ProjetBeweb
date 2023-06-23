from models.User import User

class Apprenant(User):
    def __init__(self, id, nom, prenom, pseudo, adresse, rib, secu, email, telephone, password_hash, formation, section):
        super().__init__(id, nom, prenom, pseudo, email, telephone, password_hash, section)
        self.adresse = adresse
        self.rib = rib
        self.secu = secu
        self.formation = formation

<<<<<<< HEAD
=======
    def set_password(self, password):
        # Hasher le mot de passe et le stocker sous forme de hachage sécurisé
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def get_password_hash(self):
            return self.password_hash

    def check_password(self, password):
        # Vérifier si le mot de passe fourni correspond au mot de passe haché stocké
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)
>>>>>>> origin/test
