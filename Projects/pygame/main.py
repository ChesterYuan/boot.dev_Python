# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return screen
    
def game_loop(screen):
    running = True
    while running:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen
        screen.fill((0, 0, 0))
        
        # Update the display
        pygame.display.flip()


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initialize the game
    screen = initialize_game()
    
    # Run the game loop
    game_loop(screen)
    
    # Clean up
    pygame.quit()

if __name__ == "__main__":
    main()