from CircleShape import CircleShape


import pygame


import random


class Particle(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.lifetime = random.uniform(0.1, 0.5)

    def update(self, dt):
        self.position += self.velocity * dt
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)