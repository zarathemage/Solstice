import pygame

from room import *
from roomcrossroad1tilemap import *

from underdarkroom1 import *

class RoomCrossRoad1(Room):
    def __init__(self):
        Room.__init__(self,0,0)
        self.image = pygame.image.load("./pics/solstice-roomcrossroad-0.png")

        self.tilemap = RoomCrossRoad1Tilemap()
        
    def collide(self, x,y):
        1 ### FIXME

    def blit(self, screen):
###        screen.blit(self.image, [self.x, self.y])

        self.tilemap.blit(screen)


    def exit(self, player):
        if player.x > 350: ### FIXME
            return UnderdarkRoom1()
        else:
            return None
