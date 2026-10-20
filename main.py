import pygame

from constants import PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    print("Hello from asteroid-game!")
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt: float = 0.0

    # hold all objects that can be updated
    updatable = pygame.sprite.Group()

    # hold all objects that can be drawn
    drawable = pygame.sprite.Group()

    # add Player class to the updatable and drawable groups
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game Loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for drawing in drawable:
            drawing.draw(screen)
        dt = clock.tick(60) / 1000
        # print(dt)
        updatable.update(dt)
        pygame.display.flip()


if __name__ == "__main__":
    main()
