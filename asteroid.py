from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        # 1. kill self
        self.kill()
        # 2. if too small, return
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # 3. pick angle a = random.uniform 20,50
            random_angle = random.uniform(20, 50)
            # 4. v1 = velocity rotated by +a; v2 = velocity rotated by -a
            velocity1 = pygame.Vector2.rotate(self.velocity, random_angle)
            velocity2 = pygame.Vector2.rotate(self.velocity, -random_angle)
            # 5. new_radius is old_radius - ASTEROID_MIN_RADIUS
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            # 6. create asteroid A at current pos, with new radius; set velocity to v1 * 1.2
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = velocity1 * 1.2
            # 7. do the same for asteroid B v2 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2.velocity = velocity2 * 1.2

            



            

            

