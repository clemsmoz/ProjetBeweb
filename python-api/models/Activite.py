<<<<<<< HEAD
from models.Formation import Formation

class Activite(Formation):
    def __init__(self, id, titre, contenu, formation):
        super().__init__(id, titre, contenu)
        self.formation = formation

    def get_formation(self):
=======
from models.Formation import Formation

class Activite(Formation):
    def __init__(self, id, titre, contenu, formation):
        super().__init__(id, titre, contenu)
        self.formation = formation

    def get_formation(self):
>>>>>>> 706f18afd9c9d68616a44f9f73cec89ac68481aa
        return self.formation