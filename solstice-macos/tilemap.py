class TileMap:
    def __init__(self):
        self.map = []

        self.tilewidth = 48
        self.tileheight = 48

        self.mapwidth = 5
        self.mapheight = 5

        self.x = 240 ### offset of drawing room tiles
        self.y = 240
        
    def getcurrenttile(self, player):
        ### kludge : test left,right,up and down tile
        for t in self.map:
            if player.matchTile(t):
                return t

        return None
