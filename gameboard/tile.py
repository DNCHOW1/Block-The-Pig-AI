import pygame
from collections import OrderedDict

class Tile():
    def __init__(self, doubleCoord, loc, blocked=False):
        self.neighbors = OrderedDict()
        self.blocked = blocked
        self.CP = doubleCoord
        self.mouse_loc = loc
        self.x = loc[0]
        self.y = loc[1]

    def getCP(self):
        return self.CP

    def __repr__(self):
        return f"{self.blocked}"
