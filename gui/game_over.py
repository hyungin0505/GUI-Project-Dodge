def init(w):
    w.data.game_over = w.newImage(
        x = (1200-480)/2,
        y = (800-128)/2,
        filename= './assets/images/game_over.png',
        new_width=480,
        new_height=128,
        isVisible=False,
        isPixelwiseModifiable=False
    )