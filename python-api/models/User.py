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
<<<<<<< HEAD
=======

    def get_id(self):
        return self.id
>>>>>>> 706f18afd9c9d68616a44f9f73cec89ac68481aa

<<<<<<< HEAD
    def get_id(self):
        return self.id

    def get_full_name(self):
        return f"{self.prenom} {self.nom}"

    def get_pseudo(self):
        return f"{self.pseudo}"

    def get_password_hash(self):
        return self.password_hash
    
    def set_password(self, password):
        # Hasher le mot de passe et le stocker sous forme de hachage sécurisé
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
=======
    def get_full_name(self):
        return f"{self.prenom} {self.nom}"

    def get_pseudo(self):
        return f"{self.pseudo}"

    def get_password_hash(self):
        return self.password_hash
<<<<<<< HEAD
>>>>>>> origin/test
=======
    
    def set_password(self, password):
        # Hasher le mot de passe et le stocker sous forme de hachage sécurisé
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
>>>>>>> 706f18afd9c9d68616a44f9f73cec89ac68481aa
        
    def check_password(self, password):
        # Vérifier si le mot de passe fourni correspond au mot de passe haché stocké
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)
