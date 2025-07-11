import pygame
from constants import *
from player import Player

def main():
    pygame.init()  # Initialize the pygame library
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  # Create a clock object to control the frame rate
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")  
    dt = 0 # Initialize delta time
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player=Player(x, y) 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
           
        screen.fill("black") # Fill the screen with black
        player.draw(screen)
        pygame.display.flip() #Refresh the screen, should run last
        dt = clock.tick(60)/1000  # Control the frame rate to 60 FPS
             
         


if __name__ == "__main__":
    main()