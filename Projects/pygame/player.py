import pygame
from circleshape import CircleShape
from constants import *
from bullet import Bullet


class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.add(*self.containers)
        self.shooting_cooldown = 0
        self.lives = 3
        self.respawn_cooldown = 0
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        # If player is respawning, update respawn cooldown, player cannot move
        if self.respawn_cooldown > 0:
            self.respawn_cooldown -= dt
            if self.respawn_cooldown < 0:
                self.respawn_cooldown = 0
            return
        keys = pygame.key.get_pressed()
        # Handle movement keys
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
            self.shooting_cooldown = 0.1
        self.shooting_cooldown -= dt
        if self.shooting_cooldown < 0:
            self.shooting_cooldown = 0

    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, -1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        if self.respawn_cooldown > 0:
            # Blink: only draw if in certain phase of cooldown
            if int(self.respawn_cooldown * 5) % 2 == 0:
                return
        pygame.draw.polygon(screen, (129, 216, 208), self.triangle(), width=2)

    def shoot(self):
        if self.shooting_cooldown > 0:
            return
        bullet = Bullet(self.position.x, self.position.y, SHOT_RADIUS)
        bullet.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        return bullet

    def respawn(self):
        self.position = pygame.Vector2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.rotation = 0
        self.respawn_cooldown = 3
        print(f"Respawning in {self.respawn_cooldown} seconds...")
    


        
    


        
