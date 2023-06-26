from models.Formation import Formation

class Activite(Formation):
    def __init__(self, id_activite, titreActivite, resumeActivite, formation):
        super().__init__(id_activite, titreActivite, resumeActivite)
        self.formation = formation
        self.id_activite = id_activite
        self.titreActivite = titreActivite
        self.resumeActivite = resumeActivite

    def get_formation(self):
        return self.formation