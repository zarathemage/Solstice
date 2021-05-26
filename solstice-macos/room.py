import pygame

from tilemap import *

class Room:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.image = None ### pygame.image.load("")

        self.tilemap = None
        
    def collide(self, x,y):
        pass

    def exit(self, player):
        return None
