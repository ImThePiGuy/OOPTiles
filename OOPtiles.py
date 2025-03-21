"""
The Object Oriented Program Tile Project
"""

class Tile:
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def __str__(self):
        return f"X:{self.xpos},Y:{self.ypos}"
        
class Board:
    
    def __init__(self):
        self.tiles = []
        self.genTiles()
        self.adjTiles()

    def genTiles(self):
        for x in range(7):
            self.tiles.append([])
            for y in range(5):
                self.tiles[x].append(str(Tile(x, y)))
                
    def adjTiles(self):
        for tile in self.tiles:
            print(self.tiles[tile])
        
My_Board = Board()
#print(My_Board.tiles)
