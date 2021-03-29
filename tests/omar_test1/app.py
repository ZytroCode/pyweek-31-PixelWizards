import pygame
from win32api import GetSystemMetrics
import sys

pygame.init()

class App():
    def __init__(self,
        title: str = "Window",
        width: int = int(GetSystemMetrics(0)*0.8),
        height: int = int(GetSystemMetrics(1)*0.8),
        fps: int = 60
        ):

        self.width = width
        self.height = height
        self.size = (width, height)

        self.sprites = []
        
        self.fps = 60
        self._func = None
        self.window = pygame.display.set_mode(self.size)
        self.set_title(title)
    
    def set_title(self, title: str):
        pygame.display.set_caption(title)

    def draw_sprite(self, sprite):
        self.sprites.append(sprite)

    def update(self, func):
        def wrapper(*args, **kwargs):
            self._func = func(*args, **kwargs)
            return self._func
        
        self._func = func
        return wrapper

    def run(self):
        clock = pygame.time.Clock()

        # The game loop
        while True:

            # Checking for pygame events
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.close()
            
            # Calling the users update function
            if self._func != None:
                self._func()

            # Drawing objects on the screen
            for sprite in self.sprites:
                self.window.blit(sprite.image, sprite.position)

            self.sprites = []

            pygame.display.update()
            clock.tick(self.fps)
    
    def close(self):
        pygame.quit()
        sys.exit()
