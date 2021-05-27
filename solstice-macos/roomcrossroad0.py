import pygame

from room import *
from roomcrossroad0tilemap import *

from underdarkroom0 import *

class RoomCrossRoad0(Room):
    def __init__(self):
        Room.__init__(self,0,0)
        self.image = pygame.image.load("./pics/solstice-roomcrossroad-0.png")

        self.tilemap = RoomCrossRoad0Tilemap()
        
    def collide(self, x,y):
        1 ### FIXME

    def blit(self, screen):
###        screen.blit(self.image, [self.x, self.y])

        self.tilemap.blit(screen)


    def exit(self, player):
        if player.x > 350: ### FIXME
            return UnderdarkRoom0()
        else:
            return None
