import pygame
import sys
import snake
import fruit
import time

class Game:
    def __init__(self, window_width=720, window_height=480, snake_speed=15):
        # Inicjalizacja Pygame
        pygame.init()
        
        # Parametry okna gry
        self.window_width = window_width
        self.window_height = window_height
        self.game_window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption('Snake Game')
        
        # Kolory
        self.black = pygame.Color(0, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.white = pygame.Color(255, 255, 255)
        
        # Czcionka
        self.font = pygame.font.SysFont('times new roman', 20)

        # Wynik
        self.score = 0
        
        # Prędkość gry
        self.fps = pygame.time.Clock()
        
        # Tworzenie instancji węża i owocu
        self.snake = snake.Snake([100, 50], snake_speed)
        self.fruit = fruit.Fruit(self.window_width, self.window_height)
    
    def show_score(self):
        """Wyświetla aktualny wynik."""
        score_surface = self.font.render(f'SCORE: {self.score}', True, self.white)
        score_rect = score_surface.get_rect()
        self.game_window.blit(score_surface, score_rect)
    
    def game_over(self):
        self.game_window.fill(self.black)
        game_over_surface = self.font.render(f'Your Score is: {str(self.score)}', True, self.white)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (self.window_width / 2, self.window_height / 4)
        self.game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        time.sleep(5)
        pygame.quit()
        quit()

    
    def handle_events(self):
        """Obsługuje zdarzenia w grze."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_to = 'UP'
                elif event.key == pygame.K_DOWN:
                    self.snake.change_to = 'DOWN'
                elif event.key == pygame.K_LEFT:
                    self.snake.change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_to = 'RIGHT'
    
    def check_collision(self):
        """Sprawdza kolizję węża z owocem."""
        if self.snake.position == self.fruit.position:
            self.score += 10
            self.snake.snake_body.append(self.snake.snake_body[-1])  # Wzrost długości węża
            self.fruit.position = self.fruit.generate_new_position()

        for block in self.snake.snake_body[1:]:
            if self.snake.position[0] == block[0] and self.snake.position[1] == block[1]:
                self.game_over()



    def update(self):
        """Aktualizuje stan gry."""
        # Ruch węża
        self.snake.move(self.window_width, self.window_height)
        
        # Czyszczenie ekranu
        self.game_window.fill(self.black)
        
        # Rysowanie obiektów
        self.snake.draw(self.game_window, self.green)
        self.fruit.draw(self.game_window)
        
        # Wyświetlanie wyniku
        self.show_score()
        
        # Aktualizacja ekranu
        pygame.display.update()
        
        # Kontrola prędkości gry
        self.fps.tick(self.snake.speed)
    
    def run(self):
        """Uruchamia główną pętlę gry."""
        while True:
            self.handle_events()
            self.check_collision()
            self.update()


if __name__ == "__main__":
    # Tworzenie instancji gry i uruchomienie
    game = Game()
    game.run()
