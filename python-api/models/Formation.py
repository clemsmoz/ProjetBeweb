class Formation:
    def __init__(self, id, titre, contenu):
        self.id = id
        self.titre = titre
        self.contenu = contenu

    def get_id(self):
        return self.id
    
    def get_titre(self):
        return self.titre
    
    def get_contenu(self):
        return self.contenu