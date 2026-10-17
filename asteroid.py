import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS, ASTEROID_KINDS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x:float, y: float, radius:float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += 0.01 * (self.velocity * dt/6)

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            
            avect = self.velocity.rotate(random.uniform(20,50))
            bvect = self.velocity.rotate(random.uniform(20,50))
            # ====================
            asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            asteroid1.velocity = avect * 1.5
            asteroid2.velocity = bvect * 1.5


