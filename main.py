import sys
import pygame
import player
import asteroid
import asteroidfield
from constants import *

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable,)
    player.Shot.containers = (shots, updatable, drawable)
    
    rocks = asteroidfield.AsteroidField()
    ship = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color('black'))

        updatable.update(dt)
        for rock in asteroids:
            if rock.collides(ship):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if rock.collides(shot):
                    rock.split()
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
