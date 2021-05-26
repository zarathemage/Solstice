###import math

class Tile:
    def __init__(self,x,y,z,w,h):
        self.x = x
        self.y = y
        self.z = z
        self.w = w ### maximum width of diamond tile
        self.h = h ### maximum height of diamond tile

    def collidexy(self, player, tilemap):
        ### FIXME coords of player and move to parallellogram boundary coords
        if type(player.lastmove).__name__ == 'LeftMove': ### left up
            if self.diagonalSolutionLeftDiagonal(tilemap.y+self.y,tilemap.y+self.y+self.h,
                                     tilemap.x+self.x,tilemap.x+self.x+self.w,
                                    player.x, 
                                    player.y) and self.diagonalSolutionRightDiagonal(tilemap.y+self.y,tilemap.y+self.y+tilemap.tileheight,
                                    tilemap.x+self.x+tilemap.tilewidth*2,tilemap.x+self.x+tilemap.tilewidth,
                                    player.x, 
                                    player.y):
                return True
            else:
                return False
        if type(player.lastmove).__name__ == 'RightMove':
            if self.diagonalSolutionLeftDiagonal(self.y+self.h/2,self.y+self.h,
                                    self.x+self.w,self.x+self.w/2,
                                    player.x+player.width, 
                                    player.y+player.height) and self.diagonalSolutionRightDiagonal(self.y+self.h/2,self.y+self.h,
                                     self.x,self.x+self.w/2,
                                    player.x, 
                                    player.y):
                return True
            else:
                return False
        if type(player.lastmove).__name__ == 'UpMove':
            if self.diagonalSolutionLeftDiagonal(self.y,self.y+self.h/2,
                                    self.x+self.w/2,self.x+self.w,
                                    player.x+player.width, 
                                    player.y) and self.diagonalSolutionRightDiagonal(self.y+self.h/2,self.y+self.h,
                                     self.x,self.x+self.w/2,
                                    player.x, 
                                    player.y):
                return True
            else:
                return False
        if type(player.lastmove).__name__ == 'DownMove':
            if self.diagonalSolutionLeftDiagonal(self.y+self.h,self.y+self.h/2,
                                    self.x+self.w/2,self.x+self.w,
                                    player.x, 
                                    player.y+player.height) and self.diagonalSolutionRightDiagonal(self.y+self.h/2,self.y+self.h,
                                     self.x,self.x+self.w/2,
                                    player.x, 
                                    player.y):
                return True
            else:
                return False

        return False

    ### check player x,y over left diagonal of parallellogram
    def diagonalSolutionLeftDiagonal(self, y2,y1,x2,x1,playerx,playery):
        dy = y2 - y1
        dx = x2 - x1
        d = dy/dx

        if (abs(d*(playerx - x1) - (playery - y1)) > 0):
            return True
        else:
            return False

    ### check player x,y over right diagonal of parallellogram
    def diagonalSolutionRightDiagonal(self, y2,y1,x2,x1,playerx,playery):
        dy = y2 - y1
        dx = x2 - x1
        d = dy/dx

        if (abs(d*(playerx - x1) - (playery - y1)) > 0):
            return True
        else:
            return False
        
    ### Test collision with x,y,z
    def collidez(self, player, tilemap):
        if (self.collidexy(player, tilemap) and player.z < self.z):
            return True
        else:
            return False
