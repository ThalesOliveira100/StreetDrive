import random
from code.const import WIN_WIDTH, WIN_HEIGHT, PLAYER_POSITION
from code.enemy import Enemy
from code.golden_star import GoldenStar
from code.health_pack import HealthPack
from code.player import Player
from code.player_boost import PlayerBoost


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        enemy_choise = random.choice([1, 2])
        choised_enemy = f'Enemy{enemy_choise}'

        match entity_name:
            case 'Player':
                return Player('Player', PLAYER_POSITION)

            case 'Enemy':
                return Enemy(name=choised_enemy, position=(random.randint(400, 565), -50))

            case 'Health':
                return HealthPack(name='Health', position=(random.randint(400, 565), -50))

            case 'GoldenStar':
                return GoldenStar(name='GoldenStar', position=(random.randint(400, 565), -50))
