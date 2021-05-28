import pygame

from room import *
from crossroadroom1tilemap import *

from underdarkroom1 import *
from underdarkroom2 import *

from movethroughdoorloopobject import *

class CrossRoadRoom1(Room):
    def __init__(self):
        Room.__init__(self,0,0)
        self.image = pygame.image.load("./pics/crossroadroom1-bg-3.png")

        self.tilemap = CrossRoadRoom1Tilemap()
        
    def collide(self, x,y):
        1 ### FIXME

    def blit(self, screen):
        screen.blit(self.image, [186,55])

        self.tilemap.blit(screen)


    def exit(self, player, screen):
        if player.x > 350: ### FIXME
            ### play movie of walking through door
            o = MoveThroughDoorLoopObject()
            o.move_mainloop(player, self, screen)
            
            return UnderdarkRoom2()
        elif player.x < 83 and player.y > 205 and player.y < 305:
            ### play movie of walking through door
            o = MoveThroughDoorLoopObject()
            o.move_mainloop(player, self, screen)            

            return UnderdarkRoom1()
        else:
            return None

