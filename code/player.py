import pygame.key

import code.const
from code.const import ENTITY_SPEED, WIN_WIDTH, WIN_HEIGHT, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, \
    PLAYER_KEY_LEFT_A, PLAYER_KEY_RIGHT_D, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_UP_W, PLAYER_KEY_DOWN_S
from code.entity import Entity
from code.player_boost import PlayerBoost


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name=name, position=position, tipo='Player')
        self.base_speed = ENTITY_SPEED[self.name]  # Velocidade base
        self.boost_multiplier = 3  # Multiplicador para o turbo
        self.boost_active = False
        self.boost_speed = self.base_speed * self.boost_multiplier
        self.boost_effect = None

        self.golden_star_count = 0

    def move(self):
        pressed_key = pygame.key.get_pressed()

        # Ativa o boost ao pressionar espaço
        # Ativa ou desativa o boost
        if pressed_key[pygame.K_SPACE] and self.rect.top > 5:
            self.rect.centery -= 0.6
            self.boost_active = True
        else:
            self.boost_active = False

        self.speed = self.boost_speed if self.boost_active else self.base_speed  # Inicializa a velocidade normal

        if (pressed_key[PLAYER_KEY_LEFT[self.name]] or pressed_key[PLAYER_KEY_LEFT_A[self.name]]) and self.rect.left > 400:
            self.rect.centerx -= self.speed

        if (pressed_key[PLAYER_KEY_RIGHT[self.name]] or pressed_key[PLAYER_KEY_RIGHT_D[self.name]]) and self.rect.right < 615:
            self.rect.centerx += self.speed

        if (pressed_key[PLAYER_KEY_UP[self.name]] or pressed_key[PLAYER_KEY_UP_W[self.name]]) and self.rect.top > 5:
            self.rect.centery -= self.speed

        if (pressed_key[PLAYER_KEY_DOWN[self.name]] or pressed_key[PLAYER_KEY_DOWN_S[self.name]]) and self.rect.bottom < (WIN_HEIGHT - 5):
            self.rect.centery += self.speed

        if self.boost_active and self.boost_effect:
            self.boost_effect.rect.centerx = self.rect.centerx  # Centraliza horizontalmente
            self.boost_effect.rect.top = self.rect.bottom

    def boost(self):
        """Garante que o boost é criado apenas uma vez"""
        if self.boost_active:
            if not self.boost_effect:  # Se ainda não foi criado
                self.boost_effect = PlayerBoost(name="boost01", position=(self.rect.centerx, self.rect.bottom),
                                                tipo="Boost")
                return self.boost_effect
        return None  # Não retorna um novo boost se já existir
