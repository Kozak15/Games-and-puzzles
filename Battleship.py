#Battleship Game Simulation
import random
def make_grid(n):
    return [[0 for _ in range(n)] for _ in range(n)]
#Ship Class
class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0
    def place(self, grid):
        n = len(grid)
        placed = False
        while not placed:
            orientation = random.choice(['H', 'V'])
            if orientation == 'H':
                row = random.randint(0, n-1)
                col = random.randint(0, n - self.size)
                if all(grid[row][col+i] == 0 for i in range(self.size)):
                    for i in range(self.size):
                        grid[row][col+i] = 1
                        self.positions.append((row, col+i))
                    placed = True
            else:
                row = random.randint(0, n - self.size)
                col = random.randint(0, n-1)
                if all(grid[row+i][col] == 0 for i in range(self.size)):
                    for i in range(self.size):
                        grid[row+i][col] = 1
                        self.positions.append((row+i, col))
                    placed = True
#Print Grid
def print_grid(grid):
    for row in grid:
        print(''.join((str(cell)+' ') for cell in row))
#Random Hits
def random_hit(lst,grid,n_hit):
    n = len(grid)
    hits = 0
    while hits < n_hit:
        row = random.randint(0, n-1)
        col = random.randint(0, n-1)
        if grid[row][col] == 1:
            grid[row][col] = 'X'
            lst.append((row, col, 'Hit'))
            hits += 1
        elif grid[row][col] == 0:
            grid[row][col] = 'O'
            lst.append((row, col, 'Miss'))  
#Main Function, takes in number of ships and grid size. Grid is n x n  
def main(n_ships,n_grid):
    attacks = []
    grid = make_grid(n_grid)
    ships = [Ship("Destroyer", 2), Ship("Submarine", 1), Ship('Cruiser',3), Ship('Battleship',4),Ship('Carrier',5)]
    for i in range(n_ships):
        ship = random.choice(ships)
        ship.place(grid)
    print('Originally')
    print_grid(grid)
    random_hit(attacks,grid,2)
    print('\nFinal')
    print_grid(grid)