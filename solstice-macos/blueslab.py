from ochreslab import *

### NOTE derives from ochre slab
class BlueSlab(OchreSlab):
    def __init__(self,x,y,z,w,h): ### NOTE z = 1 or more
        OchreSlab.__init__(self,x,y,z,w,h)

        self.image = pygame.image.load("./pics/ochreslab-blue-tile-2.png")
