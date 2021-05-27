###import math

class Tile:
    def __init__(self,x,y,z,w,h):
        self.x = x
        self.y = y
        self.z = z ### the height to jump on
        self.w = w ### maximum width of diamond tile
        self.h = h ### maximum height of diamond tile

    ### main collision method (calls collidexy method)
    def collidez(self, player, tilemap):
        pass

    ### tile collision method (without tile height, z position)
    def collidexy(self, player, tilemap):
        pass


    ### check player x,y over left diagonal of parallellogram
    def leftDiagonalSolution(self, y2,y1,x2,x1,playerx,playery):
        dy = y2 - y1
        dx = x2 - x1
        d = dy/dx

        if (d*(playerx - x1) - (playery - y1) > 0):
            return True
        else:
            return False

    ### check player x,y before right diagonal of parallellogram
    def rightDiagonalSolution(self, y2,y1,x2,x1,playerx,playery):
        dy = y2 - y1
        dx = x2 - x1
        d = dy/dx


        if (d*(playerx - x1) - (playery - y1) < 0):
            return True
        else:
            return False
