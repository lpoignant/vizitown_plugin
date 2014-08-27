import logging


class Tile:

    def __init__(self, Xmin, Ymin, Xmax, Ymax):
        self.logger = logging.getLogger('Vizitown')

        self.xmin = Xmin
        self.xmax = Xmax
        self.ymin = Ymin
        self.ymax = Ymax