import random
import pygame
from circleshape import *
from constants import *

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
		self.delay = 5

	def draw(self, screen):
		pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt
		self.delay -= dt
		if (
			self.delay <= 0
			and (self.position.x >= SCREEN_WIDTH
			or self.position.x <= 0
			or self.position.y >= SCREEN_HEIGHT
			or self.position.y <= 0)):
			self.kill()


	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		angle = random.uniform(20, 50)
		vel_1 = self.velocity.rotate(angle)
		vel_2 = self.velocity.rotate(-angle)
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		new_1 = Asteroid(self.position.x, self.position.y, new_radius)
		new_1.velocity = vel_1 * 1.2
		new_2 = Asteroid(self.position.x, self.position.y, new_radius)
		new_2.velocity = vel_2 * 1.2
