import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()  # Initialize the pygame library
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  # Create a clock object to control the frame rate
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")  
    dt = 0 # Initialize delta time
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()  # Create a group for asteroids
    shots = pygame.sprite.Group() 
    Asteroid.containers = (asteroids, updatable, drawable)   
    AsteroidField.containers = (updatable)  # Set containers for the asteroid field
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)  # Set containers for shots
    Player.containers = (updatable, drawable)
    player=Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)  # Create a player object at the center of the screen
    
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
           
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collision(asteroid):
                sys.exit("GAME OVER!")
            
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()  # Remove the shot and the asteroid
                    asteroid.split()
            

        screen.fill("black") # Fill the screen with black
                
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip() #Refresh the screen, should run last
        
        dt = clock.tick(60)/1000  # limit  the frame rate to 60 FPS
            
         


if __name__ == "__main__":
    main()