class Gameboard:

    def __init__(self):
        self.x_guide = ['', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.y_guide = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']

    def create_board(self):
        grid = [self.x_guide]
        i = 0
        j = 1
        while i < 21:
            if i == 0:
                pass
            else:
                grid.append([self.y_guide[i]])
            while j < 21:
                if i == 0:
                    break
                else:
                    grid[i].append('w')
                    j += 1
            print(grid[i])
            i += 1
            j = 1


