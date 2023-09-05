import pygame
import random

class SnakeGame:
    def __init__(self):
        self.running = False
        self.snake = [(10, 10)]
        self.food = (15, 15)
        self.direction = pygame.K_RIGHT
        self.cell_size = 30
        self.num_cells = 20
        self.snake_color = (52, 50, 25)
        self.food_color = (52, 50, 25)
        self.speed = 100  # Speed in milliseconds
        self.score = 0  # Added score attribute

    def start(self):
        self.running = True

    def handle_input(self, key):
        if key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
            self.direction = key

    def update(self):
        if not self.running:
            return

        head = self.snake[0]
        if self.direction == pygame.K_UP:
            new_head = (head[0], head[1] - 1)
        elif self.direction == pygame.K_DOWN:
            new_head = (head[0], head[1] + 1)
        elif self.direction == pygame.K_LEFT:
            new_head = (head[0] - 1, head[1])
        elif self.direction == pygame.K_RIGHT:
            new_head = (head[0] + 1, head[1])

        if new_head in self.snake or new_head[0] < 0 or new_head[1] < 0 or new_head[0] >= self.num_cells or new_head[1] >= self.num_cells:
            self.running = False
            return

        self.snake.insert(0, new_head)
        if new_head == self.food:
            self.score += 1  # Increment score
            self.food = (random.randint(0, self.num_cells - 1), random.randint(0, self.num_cells - 1))
        else:
            self.snake.pop()

    def display(self, screen, font):
        if not self.running:
            return

        # Display score
        score_surface = font.render(f'Score: {self.score}', True, (255, 255, 255))
        screen.blit(score_surface, (10, 10))

        for x in range(self.num_cells):
            for y in range(self.num_cells):
                color = self.snake_color if (x, y) in self.snake else (228, 255, 254)
                pygame.draw.rect(screen, color, pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size))

        pygame.draw.rect(screen, self.food_color, pygame.Rect(self.food[0] * self.cell_size, self.food[1] * self.cell_size, self.cell_size, self.cell_size))
