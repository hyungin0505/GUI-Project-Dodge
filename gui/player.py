def game_player_init(w):
    w.data.image_game_player = w.newImage(
        x = (1200-32)/2-16,
        y = (800-32)/2-16,
        filename = './assets/images/player.png',
        new_width=32,
        new_height=32,
        isVisible=False,
        isPixelwiseModifiable=False
    )