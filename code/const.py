import pygame
import pygame_menu
from pygame_menu import Theme

# B
BG_SCROLL_SPEED = 0.8

# C
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (255, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)
COLOR_GRAY_LIGHT = (118, 118, 118)
COLOR_GRAY = (110, 110, 110)
COLOR_FONT_WIDGET = 228, 230, 246
COLOR_BLACK = (0, 0, 0)
COLOR_ORANGE = (255, 165, 0)

# E
ENTITY_SPEED = {
    'Player': 0.7,
}
ENTITY_HEALTH = {
    'Player': 5,
    'Enemy': 1,
    'Boost': 1,
    'Props': 1
}

# M
MENU_PRINCIPAL_TEMA = Theme(
    background_color=pygame_menu.BaseImage(image_path='./assets/BG/menuBG.jpg'),
    selection_color=COLOR_YELLOW,

    # configurações do título
    title_font='comicsansms',
    title_background_color=COLOR_GRAY_LIGHT,
    title_font_color=COLOR_FONT_WIDGET,
    title_font_size=60,
    title_font_shadow=True,

    # configurações dos widgets
    widget_background_color=COLOR_GRAY_LIGHT,
    widget_border_color=COLOR_GRAY,
    widget_border_width=3,
    widget_cursor=pygame.SYSTEM_CURSOR_HAND,
    widget_font='comicsansms',
    widget_font_color=COLOR_FONT_WIDGET,
    widget_font_size=40,
    widget_margin=(5, 25),
    widget_padding=(5, 40)
)
MENU_SONG = './assets/songs/BGM.ogg'
MENU_GAME_SONG = './assets/songs/FASE_SONG.mp3'
MENU_GAMEOVER_SONG = './assets/songs/GAME_OVER_SONG.ogg'
MENU_SONG_VOLUME = 0.2
MENU_EFFECTS_SONG_VOLUME = 0.5

# P
PLAYER_POSITION = (522, 565)
PLAYER_KEY_LEFT = {'Player': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player': pygame.K_RIGHT}
PLAYER_KEY_LEFT_A = {'Player': pygame.K_a}
PLAYER_KEY_RIGHT_D = {'Player': pygame.K_d}
PLAYER_KEY_UP = {'Player': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player': pygame.K_DOWN}
PLAYER_KEY_UP_W = {'Player': pygame.K_w}
PLAYER_KEY_DOWN_S = {'Player': pygame.K_s}

# S
SPEED_MULTIPLIER = 1.01

# W
WIN_WIDTH = 960
WIN_HEIGHT = 640
