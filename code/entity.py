from abc import ABC, abstractmethod
import pygame.image
from code.const import ENTITY_HEALTH


class Entity(ABC):

    def __init__(self, tipo: str, name: str, position: tuple):
        self.name = name
        self.tipo = tipo
        try:
            self.surf = pygame.image.load(f'./assets/PNG/{tipo}/{name}.png').convert_alpha()
        except pygame.error as e:
            print(f"Erro ao carregar imagem para {name}: {e}")
            self.surf = pygame.Surface((50, 50))  # Fallback para um quadrado vazio
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.tipo]
        self.max_health = ENTITY_HEALTH[self.tipo]

    @abstractmethod
    def move(self):
        pass
