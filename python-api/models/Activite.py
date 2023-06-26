from models.Formation import Formation

class Activite(Formation):
    def __init__(self, id, titre, contenu, formation):
        super().__init__(id, titre, contenu)
        self.formation = formation
       

    def get_formation(self):
        return self.formation