import pygame
from constants import *

def main():
    pygame.init()  # Initialize the pygame library
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")  
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black") # Fill the screen with black
        pygame.display.flip() #Refresh the screen, should run last

         


if __name__ == "__main__":
    main()