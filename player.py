import pygame
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.angle = 0
        self.timer = 0

    def draw(self, screen):
        pygame.draw.polygon(
            screen,
            "white",  # Color
            self.triangle(),  # Points of triangle
            2  # Line width
        )

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED #using  vector to set speed and direction
        self.timer = PLAYER_SHOOT_COOLDOWN #setting shooting cooldown



    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED *dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
       
        self.timer -= dt

        if keys[pygame.K_a]:
            Player.rotate(self, -dt)

        if keys[pygame.K_d]:
            Player.rotate(self, dt)
        
        if keys[pygame.K_w]:
            Player.move(self,dt)
        
        if keys[pygame.K_s]:
            Player.move(self, -dt)
        
        if keys[pygame.K_SPACE]: #can only shoot if enough time has passed (0.3) seconds
            if self.timer <= 0:
                Player.shoot(self)



