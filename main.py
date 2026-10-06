import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from circleshape import CircleShape
from player import Player

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f'''Screen width: {SCREEN_WIDTH} 
    Screen height: {SCREEN_HEIGHT}''')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    #=== screen size ===
    clock = pygame.time.Clock()
    dt = 0.0
    #=== clock and tick values ===
    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    player.draw(screen)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)


if __name__ == "__main__":
    main()
