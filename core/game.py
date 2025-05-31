import random

from core.button import check_play_button_clicked
from core.debugger import d_print
from gui.enemy import Enemy
from utils import config


def game_start(w):
    check_play_button_clicked(w)
    if config.game_started == 1:
        w.showObject(w.data.image_game_player)

    enemies = []
    if config.game_started == 1:
        if random.randint(0, 10-config.enemy_spawn_tick) == 0:
            enemies.append(Enemy(w))
            config.enemy_count += 1

    if config.enemy_count == config.difficulty:
        config.enemy_spawn_tick += 1
        config.difficulty *= 2
        d_print("[Game Config Update] Enemy Spawn Tick: {}, Difficlty: {}".format(config.enemy_spawn_tick, config.difficulty))
