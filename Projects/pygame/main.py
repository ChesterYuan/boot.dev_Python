# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroidfield import *
from bullet import Bullet

def initialize_game():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    # During initialization
    background_image = pygame.image.load("blackhole.jpg").convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    return screen, clock, font, background_image
    
def game_loop(screen, clock, updatable, drawable, astroids, asteroid_field, player, bullets, font, score, background_image):
    running = True
    dt = 0  # Initialize delta time

    while running:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Clear the screen
        screen.blit(background_image, (0, 0))

        # Draw all sprites
        for sprite in drawable:
            sprite.draw(screen)

        # Update all sprites
        for sprite in updatable:
            sprite.update(dt)

        # Check for collisions
        if player.respawn_cooldown == 0:
            for asteroid in astroids:
                if player.collide(asteroid):
                    player.lives -= 1
                    if player.lives > 0:
                        player.respawn()
                    else:
                        running = False
                        print("Game Over")
                        break
        # Display respawn cooldown timer
        if player.respawn_cooldown > 0:
            respawn_text = f"Respawning in {int(player.respawn_cooldown) + 1}..."
            text_surface = font.render(respawn_text, True, (255, 255, 0))  # Yellow text
            # Center the text on the screen
            text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text_surface, text_rect)

        # Check for bullet collisions
        for bullet in bullets:
            for asteroid in astroids:
                if bullet.collide(asteroid):
                    bullet.kill()
                    # If destroy asteroid, add score
                    if asteroid.radius <= ASTEROID_MIN_RADIUS:
                        score += 100
                    asteroid.split()
                    break
        
        # Draw lives remaining at the upper left corner
        lives_text = f"Lives: {player.lives}"
        lives_surface = font.render(lives_text, True, (255, 0, 0))  # Red color for heart
        screen.blit(lives_surface, (20, 20))  # (x, y) position near the top-left

        # Draw score at the upper right corner
        score_text = f"Score: {score}"
        score_surface = font.render(score_text, True, (255, 255, 255))  # White text
        screen.blit(score_surface, (SCREEN_WIDTH - 150, 20))  # (x, y) position near the top-right
        
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
    screen, clock, font, background_image = initialize_game()

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    astroids = pygame.sprite.Group()
    asteroid_field = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    # Set containers for Player
    Player.containers = (updatable, drawable)

    # Set containers for Asteroid
    Asteroid.containers = (astroids, updatable, drawable)

    # Set containers for AsteroidField
    AsteroidField.containers = (updatable,)

    # Set containers for Bullet
    Bullet.containers = (bullets, updatable, drawable)

    # Create player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y, PLAYER_RADIUS)
    
    # Create asteroid field
    asteroid_field = AsteroidField()
    
    # Run the game loop
    score = 0
    game_loop(screen, clock, updatable, drawable, astroids, asteroid_field, player, bullets, font, score, background_image)
    
    # Clean up
    pygame.quit()

if __name__ == "__main__":
    main()