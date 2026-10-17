import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from astroidfield import AsteroidField
from logger import log_event
import sys 
from shot import Shot

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
    updatable = pygame.sprite.Group() #creates update group
    drawable = pygame.sprite.Group() #creates draw group
    asteroids = pygame.sprite.Group() #creates asteroid group
    shots = pygame.sprite.Group() #creates shooting group
    Player.containers = (updatable, drawable) # sets 'Player' to be within both groups; MUST BE DONE BEFORE THE OTHER STUF!
    Asteroid.containers = (asteroids, drawable, updatable) 
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    #=== Groups ===
    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
    field = AsteroidField()
    player.draw(screen)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill("black")
        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()
        for rock in asteroids:
            if rock.collides_with(player) == True:
                log_event("player_hit")
                print('Game over!')
                sys.exit()
        # Checks to see if any astroids collide w/ player
            for atvshot in shots:
                if atvshot.collides_with(rock) == True:
                    log_event("asteroid_shot")
                    atvshot.kill()
                    rock.split()
        dt = clock.tick(60)



if __name__ == "__main__":
    main()
