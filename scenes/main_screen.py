from gui import background_sprite, play_button_sprite, logo_sprite

def init(w):
    w.setTitle("Press 'Enter' to start")
    background_sprite.init(w)
    logo_sprite.init(w)
    play_button_sprite.init(w)