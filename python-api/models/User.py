import bcrypt

class User:
    def __init__(self, id, nom, prenom, pseudo, email, telephone, password_hash, section):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.pseudo = pseudo
        self.email = email
        self.telephone = telephone
        self.section = section
        self.password_hash = password_hash

    def get_id(self):
        return self.id

    def get_full_name(self):
        return f"{self.prenom} {self.nom}"

    def get_pseudo(self):
        return f"{self.pseudo}"

    def get_password_hash(self):
        return self.password_hash
    
    def set_password(self, password):
        # Hash du mot de passe et stockage
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
    def check_password(self, password):
        # Vérification password fourni == password haché stocké
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)
