import pygame
from circleshape import CircleShape
from constants import *


class Shot(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, SHOT_RADIUS)
		self.duration = 1

	def draw(self, screen):
		pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt
		self.duration -= dt
		if self.duration <= 0:
			self.kill()
		if self.position.x >= SCREEN_WIDTH or self.position.x <= 0:
			self.kill()
		if self.position.y >= SCREEN_HEIGHT or self.position.y <= 0:
			self.kill()
