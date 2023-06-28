from models.Formation import Formation

class Cp(Formation):
    def __init__(self, id, titre, contenu, idFK):
        super().__init__(id, titre, contenu)
        self.idFK = idFK

    def get_activite(self):
        return self.idFK