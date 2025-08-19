import pygame
import circleshape
from constants import *

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color('white'), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.rotation = 0
        self.shottime = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, pygame.Color('white'), self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self, shottime):
        if shottime <= 0:
            shot = Shot(self.position.x, self.position.y)
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity = forward * PLAYER_SHOT_SPEED
            self.shottime = 0.3
            return shot
                 
    def update(self, dt):
        self.shottime -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_j]:
            self.rotate(-dt)
        if keys[pygame.K_l]:
            self.rotate(dt)
        if keys[pygame.K_i]:
            self.move(dt)
        if keys[pygame.K_k]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot(self.shottime)