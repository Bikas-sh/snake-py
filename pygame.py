import pygame
import random

# Constants
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up the clock
clock = pygame.time.Clock()

# Define the Snake class
class Snake:
    def __init__(self):
        self.size = 1
        self.elements = [(WIDTH / 2, HEIGHT / 2)]
        self.dx = 10
        self.dy = 0

    def draw(self):
        for element in self.elements:
            pygame.draw.rect(screen, GREEN, (element[0], element[1], 10, 10))

    def move(self):
        head = (self.elements[0][0] + self.dx, self.elements[0][1] + self.dy)
        self.elements = [head] + self.elements[:-1]

    def grow(self):
        tail = self.elements[-1]
        dx = tail[0] - self.elements[-2][0]
        dy = tail[1] - self.elements[-2][1]
        if dx != 0:
            self.elements.append((tail[0] + dx, tail[1]))
        else:
            self.elements.append((tail[0], tail[1] + dy))
        self.size += 1

    def collide(self):
        head = self.elements[0]
        if head[0] < 0 or head[0] > WIDTH - 10 or head[1] < 0 or head[1] > HEIGHT - 10:
            return True
        for element in self.elements[1:]:
            if head == element:
                return True
        return False

# Define the Food class
class Food:
    def __init__(self):
        self.position = (random.randint(0, WIDTH - 10), random.randint(0, HEIGHT - 10))

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.position[0], self.position[1], 10, 10))

# Create the Snake and Food objects
snake = Snake()
food = Food()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx = -10
                snake.dy = 0
            elif event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx = 10
                snake.dy = 0
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dy = -10
                snake.dx = 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dy = 10
                snake.dx = 0

    # Clear the screen
    screen.fill(BLACK)

    # Move the Snake
    snake.move()

    # Check for collisions
    if snake.collide():
        running = False

    # Check if Snake ate the Food
    if snake.elements[0] == food.position:
        snake.grow()
        food = Food()

    # Draw the Snake and