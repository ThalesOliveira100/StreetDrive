import code

import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.background import Background
from code.const import WIN_HEIGHT, WIN_WIDTH, COLOR_GREEN, COLOR_RED, PLAYER_POSITION, \
    COLOR_ORANGE, MENU_GAME_SONG
from code.entity import Entity
from code.entity_factory import EntityFactory
from code.entity_mediator import EntityMediator
from code.player import Player


class Game:
    def __init__(self, window):
        self.window = window

        self.entity_list: list[Entity] = []

        self.player = EntityFactory.get_entity('Player')
        self.entity_list.append(self.player)

        self.spawn_timer = 0  # Tempo para spawnar um novo inimigo
        self.spawn_interval = max(8, int(30 - (code.const.BG_SCROLL_SPEED - 0.8) * 5))

        self.healt_spawn_timer = 0
        self.health_spawn_interval = 700

        self.golden_star_spawn_timer = 0
        self.golden_start_spawn_interval = 1000

        self.golden_star_count = 0
        self.revive_message = None
        self.revive_time = 0
        self.font = pygame.font.Font(None, 36)  # Fonte para o texto

        self.gameover = False
        self.score = 0

        pygame.mixer_music.load(MENU_GAME_SONG)
        pygame.mixer_music.play(-1)

    def run(self):
        pygame.mouse.set_cursor(pygame.cursors.arrow)

        bg = Background(self.window)

        clock = pygame.time.Clock()
        running = True
        start_game_time = True

        while running:
            clock.tick(70)
            self.score += 1 / 70
            bg.run()
            self.draw_health_bar(self.player)

            self.spawn_timer += 1
            self.healt_spawn_timer += 1
            self.golden_star_spawn_timer += 1

            # Criação de novos inimigos
            if self.spawn_timer >= self.spawn_interval:
                enemy = EntityFactory.get_entity('Enemy')
                self.entity_list.append(enemy)
                self.spawn_timer = 0  # Reseta o timer

            elif self.healt_spawn_timer >= self.health_spawn_interval:
                health = EntityFactory.get_entity('Health')
                self.entity_list.append(health)
                self.healt_spawn_timer = 0  # Reseta o timer

            elif self.golden_star_spawn_timer >= self.golden_start_spawn_interval:
                golden_star = EntityFactory.get_entity('GoldenStar')
                self.entity_list.append(golden_star)
                self.golden_star_spawn_timer = 0  # Reseta o timer

            # Atualiza posição das entidades
            for ent in self.entity_list:
                ent.move()
                self.window.blit(ent.surf, ent.rect)

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, Player):
                    if ent.health <= 0:
                        pygame.time.wait(250)

                        if ent.golden_star_count > 0:
                            self.reviver_jogador(ent)  # Se tiver uma Golden Star, reviver o jogador
                            pygame.time.wait(1500)
                        else:
                            self.gameover = True
                            running = False
                            pygame.mixer_music.load(code.const.MENU_GAMEOVER_SONG)
                            pygame.mixer_music.play()
                            self.show_gameover()

                    boost = ent.boost()
                    if boost and boost not in self.entity_list:  # Evita duplicação
                        self.entity_list.append(boost)

            # printed text
            self.game_text(36, f'VIDA: {self.player.health}', COLOR_ORANGE, (10, 10))
            self.game_text(36, f'ESTRELAS DOURADAS: {self.player.golden_star_count}', COLOR_ORANGE, (10, 70))
            self.game_text(24, f'Tempo: {self.format_tempo()}', COLOR_ORANGE, (WIN_WIDTH - 150, 10))
            self.game_text(24, f'fps: {clock.get_fps():.0f}', COLOR_ORANGE, (10, WIN_HEIGHT - 35))
            self.game_text(24, f'Entidades: {len(self.entity_list)}', COLOR_ORANGE, (10, WIN_HEIGHT - 20))

            self.game_text(
                24,
                'MOVIMENTO: W, A, S, D',
                COLOR_ORANGE,
                (WIN_WIDTH - 200, WIN_HEIGHT - 150))

            self.game_text(
                24,
                'NITRO: ESPAÇO',
                COLOR_ORANGE,
                (WIN_WIDTH - 200, WIN_HEIGHT - 100))

            self.game_text(
                24,
                'PAUSAR: ESC',
                COLOR_ORANGE,
                (WIN_WIDTH - 200, WIN_HEIGHT - 50))

            pygame.display.flip()

            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

            # Atualiza a tela
            pygame.display.update()

            while start_game_time:
                start_game_time = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Pausa o jogo ao pressionar ESC
                        self.show_pause_menu()

        pygame.quit()
        quit()

    def reviver_jogador(self, player):
        """Lógica de reviver o jogador com uma Golden Star"""
        if player.golden_star_count > 0:
            player.golden_star_count -= 1  # Consome a Golden Star
            player.health = player.max_health  # Restaura a saúde do jogador
            player.rect.x = PLAYER_POSITION[0]  # Reseta a posição do jogador
            player.rect.y = PLAYER_POSITION[1]
            self.revive_time = 0
            self.mostrar_mensagem_reviver()

    def mostrar_mensagem_reviver(self):
        # Exibe a mensagem de reviver na tela com contador de reinício""
        self.revive_message = "Jogador revivido com a Golden Star!"
        if self.revive_message and self.revive_time <= 120:
            self.game_text(36, self.revive_message, COLOR_ORANGE, (WIN_WIDTH / 2, WIN_HEIGHT / 2))
            pygame.display.update()
            self.revive_time += 1

    def game_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def draw_health_bar(self, player):
        bar_width = 200
        bar_height = 20
        fill = (player.health / player.max_health) * bar_width  # A barra vai se encher com base na vida do jogador
        pygame.draw.rect(self.window, COLOR_RED, (10, 40, bar_width, bar_height))  # Barra de fundo (vermelha)
        pygame.draw.rect(self.window, COLOR_GREEN, (10, 40, fill, bar_height))  # Barra de vida (verde)

    def show_pause_menu(self):
        from code.menu_pause import Pause
        pause_menu = Pause(self.window, self, 'Pausa')
        pause_menu.toggle_pause()
        pause_menu.run()

    def show_gameover(self):
        from code.gameover import GameOver
        formatted_time_value = self.format_tempo()
        gameover_menu = GameOver(self.window, formatted_time_value)  # Menu de game over
        gameover_menu.run()

    def format_tempo(self):
        """Retorna o tempo formatado"""
        minutes = int(self.score) // 60
        seconds = int(self.score) % 60
        return f"{minutes:02}:{seconds:02}"
