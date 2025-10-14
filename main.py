import sys
import random
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from explosion import Particle


def main():

#
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption("Asteroids")
	pygame.font.init()
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
	font = pygame.font.SysFont("Arial", 30)
	score = 0
	lives = 5
	game_state = "start_menu"
	running = True
	background = pygame.image.load("./images/stars.jpg").convert()
	background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
	particles = []

#screens

	def draw_start_menu():
		screen.fill((0, 0, 0))
		font = pygame.font.SysFont('arial', 40)
		title = font.render('Asteroids', True, (255, 255, 255))
		start_button = font.render('Space to Start', True, (255, 255, 255))
		screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/2 - title.get_height()/2))
		screen.blit(start_button, (SCREEN_WIDTH/2 - start_button.get_width()/2, SCREEN_HEIGHT/2 + start_button.get_height()/2))
		pygame.display.flip()

	def draw_game_over_screen():
		screen.fill((0, 0, 0))
		font = pygame.font.SysFont('arial', 40)
		title = font.render('Game Over', True, (255, 255, 255))
		restart = font.render('R - Restart', True, (255, 255, 255))
		quit = font.render('Q - Quit', True, (255, 255, 255))
		final_score = font.render(f'Final Score: {score}', True, (255, 255, 255))
		screen.blit(title, (SCREEN_WIDTH/2 - title.get_width()/2, SCREEN_HEIGHT/2 - title.get_height()/3))
		screen.blit(restart, (SCREEN_WIDTH/2 - restart.get_width()/2, SCREEN_HEIGHT/1.9 + restart.get_height()))
		screen.blit(quit, (SCREEN_WIDTH/2 - quit.get_width()/2, SCREEN_HEIGHT/2 + quit.get_height()/2))
		screen.blit(final_score, (SCREEN_WIDTH/2 - final_score.get_width()/2, SCREEN_HEIGHT/2 + final_score.get_height()*2.5))
		pygame.display.flip()


#game code
	while running:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		if game_state == "start_menu":
			draw_start_menu()
			keys = pygame.key.get_pressed()
			if keys[pygame.K_SPACE]:
				game_state = "game"
				game_over = False

		elif game_state == "game_over":
			draw_game_over_screen()
			keys = pygame.key.get_pressed()
			if keys[pygame.K_r]:
				game_state = "start_menu"
				lives = 5
				score = 0
			elif keys[pygame.K_q]:
				pygame.quit()
				quit()

		elif game_state == "game":
			screen.fill((0, 0, 0))
			screen.blit(background, (0, 0))
			for sprite in drawable:
				sprite.draw(screen)

			for u in drawable:
				if u in asteroids:
					pass
				else:
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
				if a.collision(player) == True and (lives > 0) == True:
					for a in asteroids:
						a.kill()
					lives -= 1
					player.position.x = x
					player.position.y = y
				elif a.collision(player) == True and (lives <= 0) == True:
					for a in asteroids:
						a.kill()
					player.position.x = x
					player.position.y = y
					game_over = True
					game_state = "game_over"
				for s in shots:
					if a.collision(s) == True:
						a.split()
						s.kill()
						score += 5
						lifetime = 0.5
						for i in range(15):
							particles.append(Particle(a.position.x, a.position.y, lifetime))

			for particle in particles[:]:
				particle.update(dt)
				particle.draw(screen)
				if particle.lifetime <= 0:
					particles.remove(particle)

			score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
			lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
			screen.blit(score_surface, (50, 25))
			screen.blit(lives_text, (50, 50))

			pygame.display.flip()
			ms = clock.tick(60)
			dt = ms / 1000

		elif game_over:
			game_state = "game_over"
			game_over = False


#	print("Starting Asteroids!")
#	print(f"Screen width: {SCREEN_WIDTH}")
#	print(f"Screen height: {SCREEN_HEIGHT}")




if __name__ == "__main__":
    main()
