import random

import code.const
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name=name, position=position, tipo='Enemy')
        self.speed_multiplier = code.const.SPEED_MULTIPLIER / 2
        self.base_speed = code.const.SPEED_MULTIPLIER + random.uniform(0.5, 2.5)

        print(
            f'inimigo gerado com a base_speed de {self.base_speed:.2f}, '
            f'bg_speed: {code.const.SPEED_MULTIPLIER:.2f}, '
            f'speed_multiplier: {self.speed_multiplier}'
        )

    def move(self):
        self.rect.y += self.base_speed  # Move para baixo
