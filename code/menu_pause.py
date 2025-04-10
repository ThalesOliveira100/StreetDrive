import pygame_menu

from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_PRINCIPAL_TEMA


class Pause:
    def __init__(self, window, game, name):
        self.window = window
        self.game = game
        self.is_paused = False
        self.name = name

        self.pause_menu = pygame_menu.Menu(
            name,
            WIN_WIDTH,
            WIN_HEIGHT,
            theme=MENU_PRINCIPAL_TEMA,
            mouse_motion_selection=True
        )

        # Botões do submenu de pausa
        if name == 'Pausa':
            self.pause_menu.add.button('Continuar', self.resume_game)
        self.pause_menu.add.button('Reiniciar', self.restart_game)
        self.pause_menu.add.button('Voltar ao Menu', self.go_to_main_menu)

    def resume_game(self):
        self.is_paused = False
        self.game.run()

    def restart_game(self):
        self.is_paused = False
        from code.game import Game
        self.game = Game(self.window)
        self.game.run()

    def go_to_main_menu(self):
        self.is_paused = False
        self.game.gameover = True
        # Cria uma nova instância do Menu e executa o menu novamente
        from code.menu import Menu
        menu = Menu()  # A chamada ao Menu que vai retornar ao menu principal
        menu.run()

    def toggle_pause(self):
        self.is_paused = not self.is_paused

    def run(self):
        if self.is_paused:
            self.pause_menu.mainloop(self.window)
