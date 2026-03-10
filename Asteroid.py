import random

import pygame

from Particle import Particle
from CircleShape import CircleShape
from Constants import ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def collide(self, other):
        distance = self.position.distance_to(other.position)
        if distance < self.radius + other.radius:
            return True
        
        return False
    
    def explode(self):
        # radialy expand a "cloud" of dust
        num_particles = 20
        for _ in range(num_particles):
            particle = Particle(self.position.x, self.position.y, 2)
            angle = random.uniform(0, 360)
            speed = random.uniform(50, 150)
            particle.velocity = pygame.Vector2(0, 1).rotate(angle) * speed
            
            # If Particle.containers is not set, we manually add to groups
            if hasattr(Particle, "containers"):
                particle.add(Particle.containers)

    def split(self):
        self.explode()
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        angle = random.uniform(20, 50)

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius / 2)
        new_asteroid_1.velocity = self.velocity.rotate(angle) * 1.2

        new_asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius / 2)
        new_asteroid_2.velocity = self.velocity.rotate(-angle) * 1.2

        new_asteroid_1.add(self.containers)
        new_asteroid_2.add(self.containers)
        

