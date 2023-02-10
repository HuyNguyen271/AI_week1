import pygame 
from random import randint
pygame.init()

WITCH = 400
HEIGHT = 600
screen= pygame.display.set_mode((WITCH,HEIGHT))
pygame.display.set_caption("Flappy Bird")
running = True

GREEN= (0,200,0)
BLUE = (0,0,255)
RED = (255,0,0)
BLACK = (0,0,0)
YELLOW = (255,255,0)
GRAY = (128, 128, 128)
clock = pygame.time.Clock()

TUBE_WITCH = 50
TUBE_VELOCITY = 3
TUBE_GAP = 150

tube1_x = 600
tube2_x = 800
tube3_x = 1000

tube1_height = randint(100,400)
tube2_height = randint(100,400)
tube3_height = randint(100,400)

BIRD_X= 100
bird_y = 250
BIRD_WITCH = 35
BIRD_HEIGHT = 35
bird_drop_velocity = 0
GRAVITY = 0.5

score = 0
font = pygame.font.SysFont('sans',20)
tube1_pass = False
tube2_pass = False
tube3_pass = False

pausing = False

SAND_X = 0
SAND_Y = 575
SAND_WITCH = 400
SAND_HEIGHT = 35

SKY_X = 0
SKY_Y = 0
SKY_WITCH = 400
SKY_HEIGHT = 1

background_img = pygame.image.load("back.png")
bird_img = pygame.image.load("bird.png")
sand_img = pygame.image.load("sand.png")

background_img = pygame.transform.scale(background_img,(WITCH,HEIGHT))
bird_img = pygame.transform.scale(bird_img,(BIRD_WITCH,BIRD_HEIGHT))
sand_img = pygame.transform.scale(sand_img,(SAND_WITCH,SAND_HEIGHT))

while running:
	clock.tick(60)
	screen.fill(GREEN)
	screen.blit(background_img,(0,0))

#draw background
	screen.blit(background_img,(0,0))
	
# draw tube
	tube1_rect = pygame.draw.rect(screen,BLUE,(tube1_x,0,TUBE_WITCH,tube1_height))
	tube2_rect= pygame.draw.rect(screen,BLUE,(tube2_x,0,TUBE_WITCH,tube2_height))
	tube3_rect = pygame.draw.rect(screen,BLUE,(tube3_x,0,TUBE_WITCH,tube3_height))

# draw inverse
	tube1_rect_inv = pygame.draw.rect(screen,BLUE,(tube1_x,tube1_height+TUBE_GAP,TUBE_WITCH,HEIGHT - tube1_height - TUBE_GAP))
	tube2_rect_inv = pygame.draw.rect(screen,BLUE,(tube2_x,tube2_height+TUBE_GAP,TUBE_WITCH,HEIGHT - tube2_height - TUBE_GAP))
	tube3_rect_inv = pygame.draw.rect(screen,BLUE,(tube3_x,tube3_height+TUBE_GAP,TUBE_WITCH,HEIGHT - tube3_height - TUBE_GAP))
# Draw SAND and sky
	sand_rect = screen.blit(sand_img,(SAND_X,SAND_Y))
	sky_rect = pygame.draw.rect(screen,GRAY,(SKY_X,SKY_Y,SKY_WITCH,SKY_HEIGHT))
# draw bird
	# bird_rect = pygame.draw.rect(screen,RED,(BIRD_X,bird_y,BIRD_WITCH,BIRD_HEIGHT))
	bird_rect = screen.blit(bird_img,(BIRD_X,bird_y))

#bird fall
	bird_y += bird_drop_velocity
	bird_drop_velocity += GRAVITY


# move tube
	tube1_x -= TUBE_VELOCITY
	tube2_x -= TUBE_VELOCITY
	tube3_x -= TUBE_VELOCITY
# create new tube
	if tube1_x < -TUBE_WITCH:
		tube1_x = 550
		tube1_height = randint(100,400)
		tube1_pass = False
	if tube2_x < -TUBE_WITCH:
		tube2_x = 550
		tube2_height = randint(100,400)
		tube2_pass = False
	if tube3_x < -TUBE_WITCH:
		tube3_x = 550
		tube3_height = randint(100,400)
		tube3_pass = False


	score_txt = font.render("Score: " + str(score),True,BLACK)
	screen.blit(score_txt,(5,5))
# update score
	if tube1_x + TUBE_WITCH <= BIRD_X and tube1_pass == False:
		score += 1
		tube1_pass = True
	if tube2_x + TUBE_WITCH <= BIRD_X and tube2_pass == False :
		score += 1
		tube2_pass = True	
	if tube3_x + TUBE_WITCH <= BIRD_X and tube3_pass == False:
		score += 1
		tube3_pass = True

# check two rec
	for tube in [tube1_rect,tube2_rect,tube3_rect,tube1_rect_inv,tube2_rect_inv,tube3_rect_inv,sand_rect,sky_rect]:
		if bird_rect.colliderect(tube):
			pausing = True
			TUBE_VELOCITY = 0
			bird_drop_velocity = 0
			game_over_txt =  font.render("Game over, Score: " + str(score),True, BLACK)
			screen.blit(game_over_txt,(130,250))
			press_continue_txt =  font.render("Press Space to Continue !" ,True, BLACK)
			screen.blit(press_continue_txt,(110,300))		







	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
# dung space		
			if event.key == pygame.K_SPACE:
				if pausing:
					bird_y = 250
					tube1_x = 600
					tube2_x = 800
					tube3_x = 1000	
					TUBE_VELOCITY = 3
					score = 0
					pausing = False


				bird_drop_velocity = 0
				bird_drop_velocity -= 10
			
	

	pygame.display.flip()

pygame.quit()
