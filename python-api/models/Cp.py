<<<<<<< HEAD
from models.Formation import Formation

class Cp(Formation):
    def __init__(self, id, titre, contenu, activite):
        super().__init__(id, titre, contenu)
        self.activite = activite

    def get_activite(self):
=======
from models.Formation import Formation

class Cp(Formation):
    def __init__(self, id, titre, contenu, activite):
        super().__init__(id, titre, contenu)
        self.activite = activite

    def get_activite(self):
>>>>>>> 706f18afd9c9d68616a44f9f73cec89ac68481aa
        return self.activite