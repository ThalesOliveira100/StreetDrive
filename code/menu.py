import pygame
import pygame_menu

import code.const
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_PRINCIPAL_TEMA, MENU_SONG


class Menu:
    def __init__(self):
        pygame.init()
        icon = pygame.image.load('./assets/icon/icon.png')
        pygame.display.set_icon(icon)

        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

        pygame.display.set_caption("STREET DRIVE - VERSÃO 1.2.0 - RA: 4675362 | THALES OLIVEIRA")
        pygame.display.flip()

        pygame.mixer_music.load(MENU_SONG)
        pygame.mixer.music.set_volume(code.const.MENU_SONG_VOLUME)
        pygame.mixer_music.play(-1)

        self.menu = pygame_menu.Menu(
            'STREET DRIVE',
            WIN_WIDTH,
            WIN_HEIGHT,
            theme=MENU_PRINCIPAL_TEMA,
            mouse_motion_selection=True
        )

        self.menu.add.button('Jogar', self.iniciar_jogo)
        self.menu.add.button('Opções', self.exibe_opcoes)
        self.menu.add.button('Sair', pygame_menu.events.EXIT)

    def exibe_opcoes(self):
        from code.menu_options import MenuOpcoes
        menu_opcoes = MenuOpcoes(self.window)
        menu_opcoes.run()

    def run(self, *arg):
        self.menu.mainloop(self.window or arg)

    def iniciar_jogo(self):
        from code.game import Game
        game = Game(self.window)
        game.run()
