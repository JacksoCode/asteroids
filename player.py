from constants import *
from circleshape import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", Player.triangle(self), 2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_w]:
            Player.move(self, dt)
        if keys[pygame.K_a]:
            Player.rotate(self, -dt)
        if keys[pygame.K_s]:
            Player.move(self, -dt)
        if keys[pygame.K_d]:
            Player.rotate(self, dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.timer = PLAYER_SHOOT_COOLDOWN
            Player.shoot(self)

    def shoot(self):
        shot_velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = shot_velocity


