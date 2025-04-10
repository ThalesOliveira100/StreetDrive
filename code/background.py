import pygame

import code.const
from code.const import WIN_WIDTH, BG_SCROLL_SPEED, WIN_HEIGHT, SPEED_MULTIPLIER


class Background:
    def __init__(self, window):
        self.window = window
        self.bg_image = pygame.image.load('./assets/BG/street.PNG').convert()
        self.bg_width, self.bg_height = self.bg_image.get_size()
        self.bg_image = pygame.transform.scale(self.bg_image, (WIN_WIDTH, self.bg_height))
        self.bg_y1 = 0
        self.bg_y2 = -self.bg_height

        self.base_speed = BG_SCROLL_SPEED
        self.speed_multiplier = SPEED_MULTIPLIER
        self.speed_up_timer = 100  # Tempo para aumentar o speed
        self.speed_up_interval = 150  # A cada 150 frames, o speed é aumentado

    def run(self):
        self.speed_up_timer += 1

        if self.base_speed <= 10:
            if self.speed_up_timer >= self.speed_up_interval:
                self.base_speed *= self.speed_multiplier
                self.speed_up_timer = 0  # Reseta o timer
                code.const.SPEED_MULTIPLIER = self.base_speed
                code.const.BG_SCROLL_SPEED = self.base_speed

        if self.base_speed >= 2.4:
            self.speed_multiplier = 1.005
            code.const.SPEED_MULTIPLIER = 1.005

        # Mover as imagens para baixo
        self.bg_y1 += self.base_speed
        self.bg_y2 += self.base_speed

        # Resetar a posição quando sair da tela
        if self.bg_y1 >= WIN_HEIGHT:
            self.bg_y1 = -self.bg_height
        if self.bg_y2 >= WIN_HEIGHT:
            self.bg_y2 = -self.bg_height

        # Desenha as imagens na tela
        self.window.blit(self.bg_image, (0, self.bg_y1))
        self.window.blit(self.bg_image, (0, self.bg_y2))
