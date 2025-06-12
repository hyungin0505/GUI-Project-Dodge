from utils import config

def isGod(w):
    if not config.god_mode:
        w.setTitle("Avoid Enemies!! Enemies: {}".format(config.enemy_count))
    else:
        w.setTitle("GOD Mode On.. Enemies: {}".format(config.enemy_count))