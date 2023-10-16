import random

class SnakeGame:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.snake = [[5, 5], [5, 4], [5, 3]]
        self.direction = "right"
        self.paused = False
        self.food = None
        self.score = 0
        self.character_size = 20  # Character size attribute added

        self.char_snake = "#"  # Snake character
        self.char_head = "#"  # Head character
        self.char_food = "*"  # Food character
        self.char_bg = "."    # Background character
        self.speed = 100       # Game speed (milliseconds)
        
        self.spawn_food()  # Initialize the food

    def change_direction(self, key):
        # Implement logic to change the snake's direction
        if (
            key == "Up" and self.direction != "down"
            or key == "Down" and self.direction != "up"
            or key == "Left" and self.direction != "right"
            or key == "Right" and self.direction != "left"
        ):
            self.direction = key.lower()

    def toggle_pause(self):
        # Implement logic to pause/unpause the game
         self.paused = not self.paused

    def restart_game(self):
        # Implement logic to restart the game
        self.snake = [[5, 5], [5, 4], [5, 3]]
        self.direction = "right"
        self.paused = False
        self.score = 0
        self.update()

    def update(self):
        # Implement the game update logic
        if not self.paused:
            new_head = self.get_new_head()
            if new_head in self.snake or not self.is_within_bounds(new_head):
                self.restart_game()
            else:
                self.snake.insert(0, new_head)
                if new_head == self.food:
                    self.score += 1
                    self.spawn_food()
                else:
                    self.snake.pop()
                self.draw_game()
                self.root.after(self.speed, self.update)
        

    def is_within_bounds(self, position):
        # Implement logic to check if a position is within the game bounds
        return 0 <= position[0] < self.rows and 0 <= position[1] < self.columns
    
    def get_new_head(self):
        # Implement logic to calculate the new head of the snake
        head = self.snake[0]
        if self.direction == "up":
            return [head[0] - 1, head[1]]
        elif self.direction == "down":
            return [head[0] + 1, head[1]]
        elif self.direction == "left":
            return [head[0], head[1] - 1]
        elif self.direction == "right":
            return [head[0], head[1] + 1]

    def spawn_food(self):
        # Implement logic to spawn food on the game board
        while True:
            food = [random.randint(0, self.rows - 1), random.randint(0, self.columns - 1)]
            if food not in self.snake:
                self.food = food
                return

    def is_food_eaten(self):
        # Implement logic to check if the snake has eaten the food
        head = self.snake[0]
        if head == self.food:
            return True
        return False
        
