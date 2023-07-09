class Cell:
    def __init__(self, state):
        self.state = state

    def update(self, neighbors):
        # Here, you can define the rules of the automaton.
        # This is a simple example where a cell toggles its state
        # if it has exactly 2 neighbors of the same state.
        if neighbors.count(self.state) == 2:
            self.state = not self.state

class Grid:
    def __init__(self, size, pattern=None):
        self.size = size
        self.grid = [[Cell(False) for _ in range(size)] for _ in range(size)]

        if pattern is not None:
            for i in range(len(pattern)):
                for j in range(len(pattern[i])):
                    self.grid[i][j].state = pattern[i][j]

    def step(self):
        for i in range(self.size):
            for j in range(self.size):
                neighbors = [self.grid[ii % self.size][jj % self.size].state
                             for ii in [i-1, i, i+1] for jj in [j-1, j, j+1]
                             if (ii, jj) != (i, j)]
                self.grid[i][j].update(neighbors)

    def display(self):
        for i in range(self.size):
            for j in range(self.size):
                print('X' if self.grid[i][j].state else '.', end='')
            print()

# Define a simple pattern that will be replicated
pattern = [[False, True, False],
           [True, True, True],
           [False, True, False]]

# Create a grid with the given pattern
grid = Grid(10, pattern)

# Run the automaton for a few steps
for _ in range(5):
    grid.display()
    print()
    grid.step()
