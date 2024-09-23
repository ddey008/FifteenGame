import tkinter
from tkinter import messagebox
from fifteen import Fifteen

class Game:
    def __init__(self, User):
        self.User = User
        self.game = Fifteen()
        self.tiles = []
        self.User.title("Fifteen Puzzle")
        self.game.shuffle()
        self.create()
        self.score = 8
        self.updateBoard()

    def create(self):
        for i in range(4):
            row = []
            for j in range(4):
                label = tkinter.Label(self.User, text='', width=4, height=2, relief=tkinter.RIDGE, borderwidth=2)
                label.grid(row=i, column=j, padx=2, pady=2)
                label.bind('<Button-1>', lambda e, k=i, k1=j: self.tile_clicked(k, k1))
                row.append(label)
            self.tiles.append(row)

        self.restart_button = tkinter.Button(self.User, text="restart", command=self.Reset)
        self.restart_button.grid(row=self.game.size + 1, column=0, columnspan=self.game.size, padx=5, pady=5)

    def change_text(self):
        global message
        if message.get() == 'You clicked me!':
            message.set('Click me again!')
        else:
            message.set('You clicked me!')

    # Additional Features
    def Reset(self):
        self.game.shuffle()
        self.updateBoard()

    def updateBoard(self):
        for i in range(4):
            for j in range(4):
                val = self.game.tiles[4 * i + j]
                if val != 0:
                    text = str(val)
                    color = 'red'
                else:
                    text = ''
                    color = 'blue'
                if self.tiles[i][j]:
                    self.tiles[i][j].configure(text=text, foreground=color)

    def tile_clicked(self, i, j):
        empty_index = self.game.get_empty_index()
        empty_row = (empty_index // self.game.size)
        empty_col = empty_index % self.game.size
        direction = ''
        print(f"Clicked: ({i}, {j}), Empty: ({empty_row}, {empty_col})")
        if i == empty_row and j == empty_col + 1:

            direction = 'LEFT'
        elif i == empty_row and j == empty_col - 1:

            direction = 'RIGHT'
        elif i == empty_row + 1 and j == empty_col:

            direction = 'UP'
        elif i == empty_row - 1 and j == empty_col:

            direction = 'DOWN'

        if self.game.is_proper_move(direction):
            print(f"Valid move: {direction}")
            self.game.update1(direction)
            self.updateBoard()
            if self.game.is_solved():
                messagebox.showinfo("Congratulations!", "You solved the puzzle!")
        else:
            print("Invalid move")


if __name__ == "__main__":
    root = tkinter.Tk()
    app = Game(root)
    root.mainloop()
