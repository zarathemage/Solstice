import pygame

from tile import *

class Slab(Tile):
    def __init__(self,x,y,z,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.z = z
        
        self.image = None

    def blit(self, screen):
        screen.blit(self.image, [self.x, self.y])

