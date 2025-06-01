def init(w):
    w.data.player = w.newImage(
        x = (1200-32)/2,
        y = (800-32)/2,
        filename = './assets/images/player.png',
        new_width=32,
        new_height=32,
        isVisible=False,
        isPixelwiseModifiable=False
    )