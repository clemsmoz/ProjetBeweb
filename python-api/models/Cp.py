from models.Formation import Formation

class Cp(Formation):
    def __init__(self, id_cp, titreCp, contenuCp, activite):
        super().__init__(id_cp, titreCp, contenuCp)
        self.activite = activite

    def get_activite(self):
        return self.activite