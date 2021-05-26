import pygame

from tile import *

class Floor(Tile):
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.z = 0

        self.image = None

    def blit(self, screen):
        screen.blit(self.image, [self.x, self.y])
