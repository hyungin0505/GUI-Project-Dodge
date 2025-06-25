'''
import random

from core.debugger import d_print
from gui.enemy_sprite import Enemy
from utils import config

def generate(w, enemies):
    if config.game_started == 1:
        if config.enemy_spawn_tick <= config.enemy_spawn_probability and random.randint(0, config.enemy_spawn_probability-config.enemy_spawn_tick) == 0:
            enemies.append(Enemy(w))
            config.enemy_count += 1

    if config.enemy_count >= config.difficulty:
        if config.enemy_spawn_tick < 10:
            config.enemy_spawn_tick += 1
        config.difficulty *= 1.8
        d_print("\033[91m[Game Config Update]\033[0m Enemy Spawn Tick: {}, Difficlty: {}".format(config.enemy_spawn_tick, config.difficulty))
'''

import random

from core.debugger import d_print
from gui.enemy_sprite import Enemy
from utils import config

def generate(w, enemies):
    max_chance = max(1, config.enemy_spawn_probability - config.enemy_spawn_tick)

    if random.randint(0, max_chance - 1) == 0:
        enemies.append(Enemy(w))
        config.enemy_count += 1

    if config.enemy_count >= config.difficulty:
        if config.enemy_spawn_tick < config.enemy_spawn_probability - 1:
            config.enemy_spawn_tick += 1
        config.difficulty *= 1.8

        d_print("\033[91m[Game Config Update]\033[0m Enemy Spawn Tick: {} Difficulty: {}".format(config.enemy_spawn_tick, config.difficulty))