from random import randint

class Board:
    def __init__(self):
        self.map = self.make_board()
        self.snake = []
        self.coords = self.spawn_snake()
        self.make_food()
        self.directions = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
        self.game_over = False

    def make_board(self):
        arr = []
        for y in range(0, 800, 32):
            arr.append([])
            for x in range(0, 800, 32):
                arr[-1].append(Pixel((x + (x // 32 * 3) + 3, y + (y // 32 * 3) + 3)))
        return arr

    def spawn_snake(self):
        x, y = 10, 15
        pix = self.map[y][x]
        pix.type = 'snake'
        self.snake.append(pix)
        return (x, y)

    def make_food(self):
        arr = [pix for row in self.map for pix in row if pix.type == 'empty']
        pix = arr[randint(0, len(arr) - 1)]
        pix.type = 'food'


    def move(self, dir):
        move = self.directions[dir]
        x, y = self.coords[0] + move[0], self.coords[1] + move[1]

        if 0 <= y < 25 and 0 <= x < 25:
            pix = self.map[y][x]
            if pix.type == 'food':
                self.make_food()
            elif pix.type == 'snake':
                self.game_over = True
            else:
                self.snake.pop(0).type = 'empty'
            self.snake.append(pix)
            pix.type = 'snake'
            self.coords = (x, y)
        else:
            self.game_over = True

class Pixel:
    def __init__(self, pos):
        self.pos = pos
        self.type = 'empty'
