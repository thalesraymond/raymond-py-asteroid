import sys

import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from logger import log_event
from shot import Shot



def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    game_clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)   

    asteroid_field = AsteroidField()



    while True:
        log_state()
        dt = game_clock.tick(60) / 1000
        print(dt)

        screen.fill("black")

        updatable.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collide(shot):
                    log_event("asteroid_shot")
                    asteroid.kill()
                    shot.kill()
                    continue

            if asteroid.collide(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()


        for draw_item in drawable:
            draw_item.draw(screen)


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return




if __name__ == "__main__":
    main()
