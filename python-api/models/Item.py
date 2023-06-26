from models.Formation import Formation

class Item(Formation):
    def __init__(self, id_item, titreItem, contenuItem, module):
        super().__init__(id_item, titreItem, contenuItem)
        self.module = module
        self.id = id_item
        self.titreItem = titreItem
        self.contenuItem = contenuItem

    def get_module(self):
        return self.module