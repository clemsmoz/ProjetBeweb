from models.Formation import Formation

class Module(Formation):
    def __init__(self, id, titre, contenu, idFK):
        super().__init__(id, titre, contenu)
        self.idFK = idFK

    def get_cp(self):
        return self.idFK