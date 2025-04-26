import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.add(*self.containers)
        self.velocity = pygame.Vector2(0, 0)


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 215, 0), (self.position.x, self.position.y), self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        elif self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        elif self.position.y > SCREEN_HEIGHT:
            self.position.y = 0

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(10, 80)
        current_velocity = self.velocity
        velocity1 = current_velocity.rotate(-random_angle)*0.5
        velocity2 = current_velocity.rotate(random_angle)*0.5
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2
        return asteroid1, asteroid2

        if self.radius > ASTEROID_MIN_RADIUS:
            return self.split()
        return None
        
        

        