import pygame

from room import *
from underdarkroom0tilemap import *

class UnderdarkRoom0(Room):
    def __init__(self):
        Room.__init__(self,0,0)
        self.image = pygame.image.load("./pics/solstice-roomcrossroad-0.png")

        self.tilemap = UnderdarkRoom0Tilemap()
        
    def collide(self, x,y):
        1 ### FIXME

    def blit(self, screen):

        ###        screen.blit(self.image, [self.x, self.y])

        self.tilemap.blit(screen)

    def exit(self, player):
        if player.x > 500: ### FIXME
            return None###FIXME Room3()
        else:
            return None
