from models.Formation import Formation

class Item(Formation):
    def __init__(self, id, titre, contenu, module):
        super().__init__(id, titre, contenu)
        self.module = module
     

    def get_module(self):
        return self.module