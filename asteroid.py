from circleshape import  CircleShape
import pygame
import random
from constants import *
from logger import *
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self,screen) -> None:
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    def update(self,dt):
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50) 
        vec1 = self.velocity.rotate(angle)
        vec2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid1 =  Asteroid(self.position.x, self.position.y, new_radius)
        Asteroid1.velocity = vec1 * 1.2
        Asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        Asteroid2.velocity = vec2 * 1.2