import pygame
import random

class Fruit:
    def __init__(self, game_window_width, game_window_height):
        self.game_window_width = game_window_width
        self.game_window_height = game_window_height
        self.position = self.generate_new_position()
        self.color = pygame.Color(255, 0, 0)
        self.spawned = True

    def generate_new_position(self):
        """Generuje nową pozycję dla owocu."""
        return [random.randrange(1, (self.game_window_width // 10)) * 10,
                random.randrange(1, (self.game_window_height // 10)) * 10]

    def draw(self, game_window):
        """Rysowanie owocu."""
        pygame.draw.rect(game_window, self.color, pygame.Rect(self.position[0], self.position[1], 10, 10))
