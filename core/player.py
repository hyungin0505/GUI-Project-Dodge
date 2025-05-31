from core.debugger import d_print
from utils.config import player_speed


def move(w):
    if w.keys['w']:
        w.moveObject(w.data.image_game_player, new_x=w.getPosition(w.data.image_game_player)[0], new_y=w.getPosition(w.data.image_game_player)[1]-player_speed)
        d_print("[KeyBoard Input] Pressed 'w'.")
    elif w.keys['s']:
        w.moveObject(w.data.image_game_player, new_x=w.getPosition(w.data.image_game_player)[0], new_y=w.getPosition(w.data.image_game_player)[1]+player_speed)
        d_print("[KeyBoard Input] Pressed 's'.")
    elif w.keys['a']:
        w.moveObject(w.data.image_game_player, new_x=w.getPosition(w.data.image_game_player)[0]-player_speed, new_y=w.getPosition(w.data.image_game_player)[1])
        d_print("[KeyBoard Input] Pressed 'a'.")
    elif w.keys['d']:
        w.moveObject(w.data.image_game_player, new_x=w.getPosition(w.data.image_game_player)[0]+player_speed, new_y=w.getPosition(w.data.image_game_player)[1])
        d_print("[KeyBoard Input] Pressed 'd'.")