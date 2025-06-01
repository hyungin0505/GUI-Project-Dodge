def is_colliding(self, enemy, player):
    x1, y1 = enemy
    x2, y2 = player

    length1 = 16-3
    length2 = 32-3

    if (x1 < x2 + length2 and
            x1 + length1 > x2 and
            y1 < y2 + length2 and
            y1 + length1 > y2):
        return True
    return False