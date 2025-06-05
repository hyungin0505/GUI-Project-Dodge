from utils.config import PLAY_BUTTON_WIDTH, PLAY_BUTTON_HEIGHT


def init(w):
    w.data.play_button = w.newImage(
        x = 450,
        y = 450,
        filename = './assets/images/main_play_button.png',
        new_width=PLAY_BUTTON_WIDTH,
        new_height=PLAY_BUTTON_HEIGHT,
        isVisible=True,
        isPixelwiseModifiable=False
    )