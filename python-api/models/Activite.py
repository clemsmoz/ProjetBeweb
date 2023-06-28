from models.Formation import Formation

class Activite(Formation):
    def __init__(self, id, titre, contenu, idFK):
        super().__init__(id, titre, contenu)
        self.idFK = idFK

    def get_formation(self):
        return self.idFK
    