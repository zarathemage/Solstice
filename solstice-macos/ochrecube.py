from slab import *

class OchreCube(Slab):
    def __init__(self,x,y,z,w,h): ### NOTE z = 1 or more
        Slab.__init__(self,x,y,z,w,h)

        self.image = pygame.image.load("./pics/ochreslab-cube-2.png")

    ### Test collision with x,y,z
    def collidez(self, player, tilemap):
            if (self.collidexy(player, tilemap) and player.z < self.z):
                return True
            else:
                return False

        
    def collidexy(self, player, tilemap):
        ### FIXME
        pass
