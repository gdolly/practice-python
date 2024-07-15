class Island:
    def __init__(self):
        self.n_islands = 0
        self.visited = set()

    def number(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.traverse(grid, (i, j))
        return self.n_islands

    def traverse(self, grid, current):
        if current in self.visited:
            return
        (i, j) = current
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return

        self.visited.add(current)
        if grid[i][j] == "0":
            print("on water=", current)
            return
        if grid[i][j] == "1":
            print("on land================", current)
            before = self.n_islands
            self.traverse(grid, (i + 1, j))  #upward
            self.traverse(grid, (i - 1, j))  #downward
            self.traverse(grid, (i, j - 1))  #left
            self.traverse(grid, (i, j + 1))  #right
            # self.traverse(grid, (i - 1, j - 1))  #up_left
            # self.traverse(grid, (i - 1, j + 1))  #down_left
            # self.traverse(grid, (i + 1, j - 1))  #up_right
            # self.traverse(grid, (i + 1, j + 1))  #down_right
            after = self.n_islands
            if before == after:
                self.n_islands += 1


if __name__ == '__main__':
    print(Island().number([["1", "1", "1", "1", "0"],
                           ["1", "1", "0", "1", "0"],
                           ["1", "1", "0", "0", "0"],
                           ["0", "0", "0", "0", "0"]]))

    print(Island().number([["1", "1", "0", "0", "0"],
                           ["1", "1", "0", "0", "0"],
                           ["0", "0", "1", "0", "0"],
                           ["0", "0", "0", "1", "1"]]))
