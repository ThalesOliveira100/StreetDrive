from code.entity import Entity


class PlayerBoost(Entity):

    def __init__(self, tipo: str, name: str, position: tuple):
        super().__init__(tipo=tipo, name=name, position=position)

    def move(self):
        self.rect.centerx = 1
