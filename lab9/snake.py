import pygame

class Snake:
    def __init__(self, position, speed):
        self.position = position  # Główna pozycja węża (głowa)
        self.speed = speed  # Prędkość gry
        self.snake_body = [  # Początkowy kształt węża
            [100, 50],
            [90, 50],
            [80, 50]
        ]
        self.direction = 'RIGHT'  # Domyślny kierunek
        self.change_to = self.direction  # Tymczasowa zmiana kierunku

    def draw(self, game_window, color):
        """Rysowanie węża."""
        for pos in self.snake_body:
            pygame.draw.rect(game_window, color, pygame.Rect(pos[0], pos[1], 10, 10))

    def move(self, game_window_width, game_window_height):
        """Logika ruchu węża z warunkami periodycznymi."""
        # Aktualizacja kierunku na podstawie zmiennej tymczasowej
        if self.change_to == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        if self.change_to == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'
        if self.change_to == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        if self.change_to == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'

        # Aktualizacja pozycji głowy węża
        if self.direction == 'UP':
            self.position[1] -= 10
        if self.direction == 'DOWN':
            self.position[1] += 10
        if self.direction == 'LEFT':
            self.position[0] -= 10
        if self.direction == 'RIGHT':
            self.position[0] += 10

        # Warunki periodyczne (zawijanie pozycji głowy)
        self.position[0] %= game_window_width
        self.position[1] %= game_window_height

        # Aktualizacja ciała węża
        self.snake_body.insert(0, list(self.position))  # Dodanie nowej głowy
        self.snake_body.pop()  # Usunięcie ostatniego segmentu
