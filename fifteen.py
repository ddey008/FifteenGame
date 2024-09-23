import numpy as np


class Fifteen:

    # create a vector (ndarray) of tiles and the layout of tiles positions (a graph)
    # tiles are numbered 1-15, the last tile is 0 (an empty space)
    def __init__(self, size=4):
        self.tiles = np.array([i for i in range(1, size ** 2)] + [0])
        self.size = size

    # draw the layout with tiles:
    # +---+---+---+---+
    # | 1 | 2 | 3 | 4 |
    # +---+---+---+---+
    # | 5 | 6 | 7 | 8 |
    # +---+---+---+---+
    # | 9 |10 |11 |12 |
    # +---+---+---+---+
    # |13 |14 |15 |   |
    # +---+---+---+---+
    def draw(self):
        print("+" + "---+" * self.size)
        for i in range(self.size):
            for j in range(self.size):
                index = 4 * i + j
                if index < 16:
                    print(f"| {self.tiles[index]}", end=' ')
            print("|")
            print("+" + "---+" * self.size)

        print()  # Add an extra newline at the end
        pass

    # return a string representation of the vector of tiles as a 2d array
    # 1  2  3  4
    # 5  6  7  8
    # 9 10 11 12
    # 13 14 15
    def __str__(self):
        rtr = ""
        for i in range(self.size):
            for j in range(self.size):
                tile = self.tiles[self.size * i + j]
                # Consistent two-character width (leading space for single digits)
                if tile < 10:
                    rtr += " "
                # Print "  " for empty tiles instead of the tile value
                rtr += " " if tile == 0 else str(tile)
                # Add two spaces between tiles (except last in a row)
                if j != self.size - 1:
                    rtr += " "
            # Add newline after each row
            rtr += ' '
            rtr += '\n'

        # Add four spaces after the last tile on the last line
        return rtr

    # exchange i-tile with j-tile
    # tiles are numbered 1-15, the last tile is 0 (empty space)
    # the exchange can be done using a dot product (not required)
    # can return the dot product (not required)
    def transpose(self, i, j):

        tempTile = self.tiles[i]
        self.tiles[i] = self.tiles[j]
        self.tiles[j] = tempTile

    # checks if the move is valid: one of the tiles is 0 and another tile is its neighbor
    def is_proper_move(self, move):
        index = self.get_empty_index()
        move_index = 0
        if move == 'DOWN':
            move_index = index - self.size

        elif move == 'UP':
            move_index = index + self.size

        elif move == 'RIGHT':
            move_index = index - 1
        elif move == 'LEFT':
            move_index = index + 1

        return self.is_valid_neighbor(index, move_index)

    def is_valid_neighbor(self, index, move_index):
        size = self.size
        empty_row = index // self.size  # 3
        empty_col = index % self.size  # 3
        move_row = move_index // self.size  # 2
        move_col = move_index % self.size  # 3

        if empty_row == move_row and abs(empty_col - move_col) == 1:
            return True
        elif empty_col == move_col and abs(empty_row - move_row) == 1:
            return True
        else:
            return False

    # update the vector of tiles
    # if the move is valid assign the vector to the return of transpose() or call transpose
    def update1(self, move):
        print(f"Updating with move: {move}")
        index = self.get_empty_index()  # Returns 15
        real_index = 0
        if move == 'DOWN':
            real_index = index - self.size
        elif move == 'UP':
            real_index = index + self.size
        elif move == 'RIGHT':
            real_index = index - 1
        elif move == 'LEFT':
            real_index = index + 1

        if 0 <= real_index < len(self.tiles):
            self.transpose(real_index, index)
        else:
            raise ValueError("Invalid move")

    # shuffle tiles
    def shuffle(self):
        moves = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        for _ in range(100):
            move = np.random.choice(moves)
            try:
                self.update1(move)
            except ValueError:
                pass

    # verify if the puzzle is solved
    # Since each number is supposed to be in their corresponding index number, this works
    def is_solved(self):
        for i in range(1, 16):
            if self.tiles[i - 1] != i:
                return False
        return True

    def get_empty_index(self):
        index = -1
        for i in range((self.size) ** 2):
            if self.tiles[i] == 0:
                index = i
                break
        return index

    def is_valid_move(self, move):
        size = self.size
        index = self.get_empty_index()
        move_index = self.get_index(move)
        empty_row = index // self.size  # 3
        empty_col = index % self.size  # 3
        move_row = move_index // self.size
        move_col = move_index % self.size

        if empty_row == move_row and abs(empty_col - move_col) == 1:
            return True
        elif empty_col == move_col and abs(empty_row - move_row) == 1:
            return True
        else:
            return False

    def get_index(self, move):
        index = -1
        for i in range(16):
            if self.tiles[i] == move:
                index = i
                break
        return index

    def update(self, move):
        index = self.get_empty_index()
        move_index = self.get_index(move)
        if self.is_valid_move(move) == True:
            self.transpose(index, move_index)


if __name__ == '__main__':
    game = Fifteen()
    game.update(15)
    print(str(game))
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
