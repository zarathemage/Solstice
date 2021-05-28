from floor import *

class BlueFloor(Floor):
    def __init__(self,x,y,w,h):
        Floor.__init__(self,x,y,w,h)

        self.image = pygame.image.load("./pics/ochrefloor-blue-tile-2.png")
