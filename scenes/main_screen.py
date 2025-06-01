from gui import background, play_button

def init(w):
    background.init(w)
    play_button.init(w)

    return w.data.main_background, w.data.play_button