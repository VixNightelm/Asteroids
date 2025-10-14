import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():

#
	pygame.init()
	pygame.font.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	dt = 0
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2

#groups
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

#containers
	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (shots, updatable, drawable)

#variables
	clock = pygame.time.Clock()
	field = AsteroidField()
	player = Player(x, y)
	text = pygame.font.SysFont("Arial", 30)
	score = 0


#updating
	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0, 0, 0))

		for sprite in drawable:
			sprite.draw(screen)

		for u in drawable:
			if u.position.x >= SCREEN_WIDTH:
				u.position.x = 1
			if u.position.x <= 0:
				u.position.x = SCREEN_WIDTH
			if u.position.y >= SCREEN_HEIGHT:
				u.position.y = 1
			if u.position.y <= 0:
				u.position.y = SCREEN_HEIGHT
		updatable.update(dt)


		for a in asteroids:
			if a.collision(player) == True:
				print("Game over!")
				sys.exit()
			for s in shots:
				if a.collision(s) == True:
					a.split()
					s.kill()
					score += 5

		score_surface = text.render(f"Score: {score}", True, (255, 255, 255))
		screen.blit(score_surface, (50, 25))

		pygame.display.flip()
		ms = clock.tick(60)
		dt = ms / 1000

#	print("Starting Asteroids!")
#	print(f"Screen width: {SCREEN_WIDTH}")
#	print(f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()
