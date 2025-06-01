from gui import background_sprite, play_button_sprite, logo_sprite

def init(w):
    background_sprite.init(w)
    logo_sprite.init(w)
    play_button_sprite.init(w)

    return w.data.main_background, w.data.play_button