from slab import *

class OchreCubeZ(Slab):
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
        ### FIXME coords with 4 diagonals (add blit offset for this cube class)
        offsety = - int((self.y - tilemap.y)/tilemap.tileheight) * tilemap.tileheight/2
        
        if type(player.lastmove).__name__ == 'LeftMove': ### left up
            if player.y + offsety - self.z > self.y+tilemap.tileheight and player.x < self.x+tilemap.tilewidth and self.rightDiagonalSolution(self.y+28,self.y+tilemap.tileheight/2,
                                    self.x+tilemap.tilewidth/2,self.x+tilemap.tilewidth,
                                    player.x, 
                                    player.y):
                return True
        if type(player.lastmove).__name__ == 'DownMove': ### left down
            if player.y + offsety - self.z < self.y+tilemap.tileheight/2 and player.x < self.x+tilemap.tilewidth and self.rightDiagonalSolution(self.y+28,self.y+tilemap.tileheight/2,
                                    self.x+tilemap.tilewidth/2,self.x,
                                    player.x, 
                                    player.y+player.height):
                return True
        if type(player.lastmove).__name__ == 'RightMove': ### right down
            if player.y + offsety - self.z > self.y+tilemap.tileheight and player.x > self.x+tilemap.tilewidth and self.leftDiagonalSolution(self.y+28,self.y+tilemap.tileheight/2,
                                    self.x+tilemap.tilewidth/2,self.x+tilemap.tilewidth,
                                    player.x+player.width, 
                                    player.y+player.height):
                return True
        if type(player.lastmove).__name__ == 'UpMove': ### right up
            if player.y + offsety - self.z > self.y+tilemap.tileheight and player.x > self.x and self.leftDiagonalSolution(self.y+28,self.y+tilemap.tileheight/2,
                                    self.x,self.x+tilemap.tilewidth/2,
                                    player.x+player.width, 
                                    player.y):
                return True
            
        return False