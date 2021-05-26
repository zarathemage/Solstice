class Move:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def move(self, player):
        player.x += self.dx
        player.y += self.dy

    def undomove(self, player):
        player.x -= self.dx
        player.y -= self.dy
