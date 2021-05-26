from slab import *

class PurpleSlab(Slab):
    def __init__(self,x,y,z,w,h):
        Slab.__init__(self,x,y,z,w,h)  ### NOTE z = 1 or more 

        self.image = pygame.image.load("")
