from logger import Logger


class Tile:

    def __init__(self, Xmin, Ymin, Xmax, Ymax):
        self.xmin = Xmin
        self.xmax = Xmax
        self.ymin = Ymin
        self.ymax = Ymax