import pygame
import random
import circleshape
from constants import *

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color('white'), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        splitangle = random.uniform(20, 50)
        angleone = self.velocity.rotate(splitangle)
        angletwo = self.velocity.rotate(-splitangle)
        radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x, self.position.y, radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, radius)
        asteroid_one.velocity = pygame.Vector2(angleone * 1.2)
        asteroid_two.velocity = pygame.Vector2(angletwo * 1.2)

    