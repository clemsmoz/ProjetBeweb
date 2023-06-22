from models.Formation import Formation

class Module(Formation):
    def __init__(self, id, titre, contenu, cp):
        super().__init__(id, titre, contenu)
        self.cp = cp

    def get_cp(self):
        return self.cp