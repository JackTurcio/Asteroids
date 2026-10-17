import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, SHOT_RADIUS, PLAYER_SHOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot

class Player(CircleShape):
    def __init__(self, x: float, y:float):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

# in the Player class
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)
        return 
    
    def rotate(self, dt: float ) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt: float) -> None:
        self.timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt * -1)
        
        if keys[pygame.K_d]:
            self.rotate((dt)) 
        
        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move((dt * -1))
        
        if keys[pygame.K_SPACE]:
            self.shoot()
        
    def move(self, dt: float) -> None:
        unit_vector = pygame.Vector2(0, 1)
        rot_vec = unit_vector.rotate(self.rotation)
        rot_speed_vec = rot_vec * PLAYER_SPEED * dt
        self.position += rot_speed_vec

    def shoot(self):
        if self.timer > 0:
            pass
        else:
            shot = Shot(self.position.x, self.position.y, PLAYER_SHOT_SPEED)
            velocity = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity = velocity * PLAYER_SHOT_SPEED
            self.timer = PLAYER_SHOOT_COOLDOWN_SECONDS
