from floor import *

class OchreFloor(Floor):
    def __init__(self,x,y,w,h):
        Floor.__init__(self,x,y,w,h)

        self.image = pygame.image.load("./pics/ochrefloor-tile-2.png")
