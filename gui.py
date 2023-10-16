import tkinter as tk
from snake import SnakeGame
from pynput import keyboard

class SnakeGameGUI:
    def __init__(self, root, game):
        self.root = root
        self.root.title("Snake Game")
        self.root.geometry("400x450")

        self.game = game
        self.game_over = False

        self.canvas = tk.Canvas(root, bg="black", width=400, height=400)
        self.canvas.pack()

        self.character_size = 20

        self.canvas.bind("<p>", self.toggle_pause)
        self.canvas.bind("<q>", self.quit_game)
        self.canvas.bind("<r>", self.restart_game)

        self.update()
        self.draw_game()

        self.game_over_label = tk.Label(
            root, text="Game Over", font=("Arial", 24), fg="red"
        )

        # Create a listener to capture arrow key events
        self.listener = keyboard.Listener(
            on_press=self.on_key_press,
            on_release=self.on_key_release
        )
        self.listener.start()

    def on_key_press(self, key):
        if not self.game_over:
            try:
                key = key.char
                if key == 'w':
                    self.game.change_direction("Up")
                elif key == 's':
                    self.game.change_direction("Down")
                elif key == 'a':
                    self.game.change_direction("Left")
                elif key == 'd':
                    self.game.change_direction("Right")
            except AttributeError:
                pass

    def on_key_release(self, key):
        pass

    def toggle_pause(self, event):
        self.game.toggle_pause()

    def quit_game(self, event):
        self.root.destroy()

    def restart_game(self, event):
        self.game.restart_game()
        self.game_over_label.pack_forget()
        self.game_over = False
        self.update()

    def update(self):
        if not self.game_over and not self.game.paused:
            new_head = self.game.get_new_head()
            if new_head in self.game.snake or not self.game.is_within_bounds(new_head):
                self.game_over = True
                self.game_over_label.pack()
            else:
                self.game.snake.insert(0, new_head)
                if self.game.is_food_eaten():
                    self.game.score += 1
                    self.game.spawn_food()
                else:
                    self.game.snake.pop()
                self.draw_game()
                self.root.after(self.game.speed, self.update)

    def draw_game(self):
        self.canvas.delete("all")
        for i in range(self.game.rows):
            for j in range(self.game.columns):
                x1, y1 = i * self.character_size, j * self.character_size
                x2, y2 = x1 + self.character_size, y1 + self.character_size
                fill_color = "black" if (i + j) % 2 == 0 else "green"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)
        for segment in self.game.snake:
            x, y = segment[0] * self.character_size, segment[1] * self.character_size
            self.canvas.create_rectangle(
                x,
                y,
                x + self.character_size,
                y + self.character_size,
                fill="blue",
            )
        if self.game.food:
            x, y = self.game.food[0] * self.character_size, self.game.food[1] * self.character_size
            self.canvas.create_oval(
                x,
                y,
                x + self.character_size,
                y + self.character_size,
                fill="red",
            )

        self.canvas.create_text(
            200, 410, text=f"Score: {self.game.score}", font=("Arial", 16), fill="white"
        )

if __name__ == "__main__":
    game = SnakeGame(20, 20)
    root = tk.Tk()
    game_gui = SnakeGameGUI(root, game)
    root.mainloop()
