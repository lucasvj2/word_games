class Tile:
    def __init__(self, letter, x, y, w, h):
        self.letter = letter
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.xc = x + w // 2
        self.yc = y + h // 2
