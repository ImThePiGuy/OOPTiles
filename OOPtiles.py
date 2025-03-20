"""
The Object Oriented Program Tile Project


From Matthew:
    
The two algorithms you’ll be implementing for this project 
is breadth first search and djikstras algorithm. To do this, you’ll
want to create a grid of tiles who have references to their
neighbors. You’ll also want to learn about queues and priority
queues. The first problem for you to solve is: how can I change
the colors of tiles within a certain radius of a given tile? 
The second problem: how can I change the color of the tiles on the 
shortest path between a-b. Both problems require the usage of a 
priority queue and your grid of tiles which contain the information 
for their connections.

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
