import random

from core.debugger import d_print
from gui.enemy_sprite import Enemy
from utils import config

def generate(w, enemies):
    if config.game_started == 1:
        if config.enemy_spawn_tick >= 10 or random.randint(0, 10-config.enemy_spawn_tick) == 0:
            enemies.append(Enemy(w))
            config.enemy_count += 1
            if not config.god_mode:
                w.setTitle("Avoid Enemies!! Enemies: {}".format(config.enemy_count))
            else:
                w.setTitle("GOD Mode On.. Enemies: {}".format(config.enemy_count))

    if config.enemy_count >= config.difficulty:
        if config.enemy_spawn_tick < 10:
            config.enemy_spawn_tick += 1
        config.difficulty *= 1.8
        d_print("[Game Config Update] Enemy Spawn Tick: {}, Difficlty: {}".format(config.enemy_spawn_tick, config.difficulty))
