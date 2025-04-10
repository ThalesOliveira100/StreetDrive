import code

import pygame

from code.const import WIN_HEIGHT
from code.enemy import Enemy
from code.entity import Entity
from code.health_pack import HealthPack
from code.player import Player
from code.golden_star import GoldenStar


class EntityMediator:
    entity_list = []
    pygame.mixer.init()

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy) or isinstance(ent, HealthPack) or isinstance(ent, GoldenStar):
            if ent.rect.top > WIN_HEIGHT:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True

        elif isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True

        elif isinstance(ent1, HealthPack) and isinstance(ent2, Player):
            valid_interaction = True

        elif isinstance(ent1, Player) and isinstance(ent2, HealthPack):
            valid_interaction = True

        elif isinstance(ent1, GoldenStar) and isinstance(ent2, Player):
            valid_interaction = True

        elif isinstance(ent1, Player) and isinstance(ent2, GoldenStar):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):

                if isinstance(ent1, HealthPack) or isinstance(ent2, HealthPack):
                    song = pygame.mixer.Sound('./assets/songs/HEALTH_SONG.ogg')
                    pygame.mixer.Sound.set_volume(song, code.const.MENU_EFFECTS_SONG_VOLUME)
                    song.play()

                    if isinstance(ent1, Player):
                        ent1.health += 1
                        ent2.health -= 1
                    if isinstance(ent2, Player):
                        ent2.health += 1
                        ent1.health -= 1

                elif isinstance(ent1, GoldenStar) or isinstance(ent2, GoldenStar):
                    song = pygame.mixer.Sound('./assets/songs/GOLDENS_STAR_SONG.wav')
                    pygame.mixer.Sound.set_volume(song, code.const.MENU_EFFECTS_SONG_VOLUME)
                    song.play()

                    if isinstance(ent1, Player):
                        ent2.health = 0
                        if ent1.golden_star_count < 3:
                            ent1.golden_star_count += 1
                    if isinstance(ent2, Player):
                        ent1.health = 0
                        if ent2.golden_star_count < 3:
                            ent2.golden_star_count += 1
                else:
                    ent1.health -= 1
                    ent2.health -= 1
                    song = pygame.mixer.Sound('./assets/songs/CRASH_SONG.ogg')
                    pygame.mixer.Sound.set_volume(song, code.const.MENU_EFFECTS_SONG_VOLUME)
                    song.play()

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        EntityMediator.entity_list = entity_list
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                if ent.tipo != 'Player':
                    entity_list.remove(ent)

                ent.surf = pygame.image.load(f'./assets/PNG/Player/player_dead.png')
