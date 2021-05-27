from ochreslab import *

class OchreDoubleHeightSlab(OchreSlab):
    def __init__(self,x,y,z,w,h): ### NOTE z = 1 or more
        OchreSlab.__init__(self,x,y,z,w,h)

        self.image = pygame.image.load("./pics/ochreslab-tile-3.png")

