from core.button import check_play_button_clicked
from gui.enemy import Enemy
from utils import config


def game_start(w):
    check_play_button_clicked(w)
    if config.game_started == 1:
        w.showObject(w.data.image_game_player)

    enemies = []
    if config.game_started == 1:
        enemies.append(Enemy(w))