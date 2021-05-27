from slab import *

class OchreSlab(Slab):
    def __init__(self,x,y,z,w,h): ### NOTE z = 1 or more
        Slab.__init__(self,x,y,z,w,h)

        self.image = pygame.image.load("./pics/ochreslab-tile-3.png")

    ### Test collision with x,y,z
    def collidez(self, player, tilemap):
            if (self.collidexy(player, tilemap) and player.z < self.z):
                return True
            else:
                return False

        
    def collidexy(self, player, tilemap):
        ### FIXME coords of player and move to parallellogram boundary coords
        if type(player.lastmove).__name__ == 'LeftMove': ### left up
            if self.leftDiagonalSolution(self.y,self.y+tilemap.tileheight,
                                    self.x+tilemap.tilewidth,self.x,
                                    player.x, 
                                    player.y) and self.rightDiagonalSolution(self.y,self.y+tilemap.tileheight,self.x+tilemap.tilewidth*2,self.x+tilemap.tilewidth,
                                    player.x, 
                                    player.y):
                return True
            
        if type(player.lastmove).__name__ == 'RightMove': ### right down
            if self.leftDiagonalSolution(self.y,self.y+tilemap.tileheight,
                                    self.x+tilemap.tilewidth,self.x,
                                    player.x+player.width, 
                                    player.y+player.height) and self.rightDiagonalSolution(self.y,self.y+tilemap.tileheight,self.x+tilemap.tilewidth*2,self.x+tilemap.tilewidth,
                                    player.x+player.width, 
                                    player.y+player.height):
                return True
            
        if type(player.lastmove).__name__ == 'UpMove': ### right down
            if self.leftDiagonalSolution(self.y,self.y+tilemap.tileheight,
                                    self.x+tilemap.tilewidth,self.x,
                                    player.x+player.width, 
                                    player.y) and self.rightDiagonalSolution(self.y,self.y+tilemap.tileheight,self.x+tilemap.tilewidth*2,self.x+tilemap.tilewidth,
                                    player.x+player.width, 
                                    player.y):
                return True
            
        if type(player.lastmove).__name__ == 'DownMove': ### left down
            if self.leftDiagonalSolution(self.y,self.y+tilemap.tileheight,
                                    self.x+tilemap.tilewidth,self.x,
                                    player.x, 
                                    player.y+player.height) and self.rightDiagonalSolution(self.y,self.y+tilemap.tileheight,self.x+tilemap.tilewidth*2,self.x+tilemap.tilewidth,
                                    player.x, 
                                    player.y+player.height):
                return True
            
                
        return False

