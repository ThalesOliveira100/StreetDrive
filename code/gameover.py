import pygame_menu

from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_PRINCIPAL_TEMA


class GameOver:
    def __init__(self, window, score):
        self.window = window
        self.score = score  # Pontuação final
        self.gameover_menu = pygame_menu.Menu(
            'GAME OVER',
            WIN_WIDTH,
            WIN_HEIGHT,
            theme=MENU_PRINCIPAL_TEMA,
            mouse_motion_selection=True
        )

        # Botões do menu de Game Over
        label_score = self.gameover_menu.add.label(f'Tempo: {score}')
        self.gameover_menu.add.button('Reiniciar', self.reiniciar_jogo)
        self.gameover_menu.add.button('Menu', self.voltar_menu)

    def reiniciar_jogo(self):
        from code.game import Game
        game = Game(self.window)
        game.run()

    def voltar_menu(self):
        from code.menu import Menu
        menu = Menu()
        menu.run(self.window)

    def run(self):
        self.gameover_menu.mainloop(self.window)
