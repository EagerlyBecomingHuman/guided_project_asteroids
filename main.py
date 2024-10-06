import sys
import pygame # type: ignore
from constants import *
from player import Player
from asteroid import Asteroid
from  asteroidfield import AsteroidField


def main():
    print(f"Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()


    Player.containers = (updatable, drawable)
    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    # x = Player(SCREEN_WIDTH) / 2
    # y = Player(SCREEN_HEIGHT) / 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updatable_object in updatable:
            updatable_object.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                sys.exit

        screen.fill("black")

        for drawable_object in drawable:
            drawable_object.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000  # limits the framerate to 60 FPS


if __name__ == "__main__":
    main()
