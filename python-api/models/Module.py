<<<<<<< HEAD
from models.Formation import Formation

class Module(Formation):
    def __init__(self, id, titre, contenu, cp):
        super().__init__(id, titre, contenu)
        self.cp = cp

    def get_cp(self):
=======
from models.Formation import Formation

class Module(Formation):
    def __init__(self, id, titre, contenu, cp):
        super().__init__(id, titre, contenu)
        self.cp = cp

    def get_cp(self):
>>>>>>> 706f18afd9c9d68616a44f9f73cec89ac68481aa
        return self.cp