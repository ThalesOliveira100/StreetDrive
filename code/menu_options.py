import pygame
import pygame_menu

import code.const
from code.const import MENU_PRINCIPAL_TEMA, WIN_HEIGHT, WIN_WIDTH


class MenuOpcoes:
    def __init__(self, window):
        self.window = window

        self.menu_opcao = pygame_menu.Menu(
            'OPÇÕES',
            WIN_WIDTH,
            WIN_HEIGHT,
            theme=MENU_PRINCIPAL_TEMA,
            mouse_motion_selection=True
        )

        self.menu_opcao.add.range_slider(
            title='Volume BGM',
            default=code.const.MENU_SONG_VOLUME*100,
            range_values=(0, 100),
            increment=1,
            onchange=self.set_novo_volume,
            value_format=lambda x: f"{int(x)}%"
        )

        self.novo_volume = code.const.MENU_SONG_VOLUME*100

        self.menu_opcao.add.range_slider(
            title='Volume Efeitos',
            default=code.const.MENU_EFFECTS_SONG_VOLUME * 100,
            range_values=(0, 100),
            increment=1,
            onchange=self.set_novo_volume_efeito,
            value_format=lambda x: f"{int(x)}%"
        )

        self.novo_volume_efeitos = code.const.MENU_EFFECTS_SONG_VOLUME * 100

        self.menu_opcao.add.button('Salvar', self.salvar)
        self.menu_opcao.add.button('Voltar', self.voltar)

    def run(self):
        self.menu_opcao.mainloop(self.window)

    def salvar(self):
        code.const.MENU_SONG_VOLUME = self.novo_volume / 100
        pygame.mixer.music.pause()
        pygame.mixer.music.set_volume(code.const.MENU_SONG_VOLUME)
        pygame.mixer.music.unpause()
        code.const.MENU_EFFECTS_SONG_VOLUME = self.novo_volume_efeitos / 100
        self.voltar()

    def voltar(self):
        from code.menu import Menu
        menu = Menu()
        menu.run()

    def set_novo_volume(self, value):
        """ Atualiza o volume conforme o slider se move. """
        self.novo_volume = int(value)

    def set_novo_volume_efeito(self, value):
        """ Atualiza o volume conforme o slider se move. """
        self.novo_volume_efeitos = int(value)
