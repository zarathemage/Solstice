from floor import *

class PurpleFloor(Floor):
    def __init__(self,x,y,w,h):
        Floor.__init__(self,x,y,w,h)

        self.image = pygame.image.load("")
