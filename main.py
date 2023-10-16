import tkinter as tk
from snake import SnakeGame
from gui import SnakeGameGUI

if __name__ == "__main__":
    game = SnakeGame(20, 20)
    root = tk.Tk()
    game_gui = SnakeGameGUI(root, game)
    root.mainloop()
