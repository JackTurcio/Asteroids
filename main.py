import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f'''Screen width: {SCREEN_WIDTH} 
    Screen height: {SCREEN_HEIGHT}''')


if __name__ == "__main__":
    main()
