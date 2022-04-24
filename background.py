
class Background():
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img


class TitleOpen(Tile):
    def __init__(self, x, y, img):
        super().__init__(x, y, img)


class TileBlock(Tile):
    def __init__(self, x, y, img):
        super().__init__(x, y, img)
