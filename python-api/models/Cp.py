from models.Formation import Formation

class Cp(Formation):
    def __init__(self, id, titre, contenu, activite):
        super().__init__(id, titre, contenu)
        self.activite = activite

    def get_activite(self):
        return self.activite