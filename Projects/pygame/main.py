# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def initialize_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    return screen, clock
    
def game_loop(screen, clock, updatable, drawable):
    running = True
    dt = 0  # Initialize delta time
    while running:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw all sprites
        for sprite in drawable:
            sprite.draw(screen)

        # Update all sprites
        for sprite in updatable:
            sprite.update(dt)
        
        # Update the display
        pygame.display.flip()

        # Limit to 60 frames per second and get delta time
        dt = clock.tick(60) / 1000  # Convert milliseconds to seconds
        # We'll use dt later for time-based movement


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initialize the game
    screen, clock = initialize_game()

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Set containers for Player
    Player.containers = (updatable, drawable)

    # Create player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y, PLAYER_RADIUS)
 
    
    # Run the game loop
    game_loop(screen, clock, updatable, drawable)
    
    # Clean up
    pygame.quit()

if __name__ == "__main__":
    main()