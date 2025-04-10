from code.entity import Entity


class GoldenStar(Entity):
    def __init__(self, name, position):
        super().__init__(name=name, position=position, tipo='Props')
        self.base_speed = 1

    def move(self):
        self.rect.y += self.base_speed
