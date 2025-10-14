import pygame
import random
from constants import *
from circleshape import *

class Particle:
	def __init__(self, x, y, lifetime):
		self.x = x
		self.y = y
		self.lifetime = lifetime
		self.velocity_x = random.uniform(-2, 2)
		self.velocity_y = random.uniform(-2, 2)

	def update(self, dt):
		self.x += self.velocity_x
		self.y += self.velocity_y
		self.lifetime -= dt

	def draw(self, screen):
		pygame.draw.circle(screen, (255, 255 ,255), (int(self.x), int(self.y)), 2)
