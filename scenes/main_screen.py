from gui import background_sprite, play_button_sprite

def init(w):
    background.init(w)
    play_button.init(w)

    return w.data.main_background, w.data.play_button