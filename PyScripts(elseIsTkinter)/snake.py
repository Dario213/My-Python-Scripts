import pygame 
import sys 
import random   

class Snake(object):
	def __init__(self):
		self.lenght = 1
		self.pos = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
		self.dir = random.choice([UP, DOWN, LEFT, RIGHT])
		self.color = (17, 24, 27) # Teal color
		self.score = 0

	def get_head_pos(self):
		return self.pos[0]

	def turn(self, point):
		if self.lenght > 1 and (point[0] * -1, point[1] * -1) == self.dir:
			return
		else:
			self.dir = point

	def move(self):
		cur = self.get_head_pos()
		x, y = self.dir
		new = (((cur[0] + (x*GRIDSIZE)) % SCREEN_WIDTH), (cur[1] + (y*GRIDSIZE)) % SCREEN_HEIGHT)
		if len(self.pos) > 2 and new in self.pos[2:]:
			self.reset()
		else:
			self.pos.insert(0, new)
			if len(self.pos) > self.lenght:
				self.pos.pop()

	def reset(self):
		self.lenght = 1
		self.pos = [((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))]
		self.dir = random.choice([UP, DOWN, LEFT, RIGHT])
		self.score = 0

	def draw(self, surface):
		for p in self.pos:
			r = pygame.Rect((p[0], p[1]), (GRIDSIZE, GRIDSIZE))
			pygame.draw.rect(surface, self.color, r)
			pygame.draw.rect(surface, (93, 216, 228), r, 1)

	def handle_keys(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.turn(UP)
				elif event.key == pygame.K_DOWN:
					self.turn(DOWN)
				elif event.key == pygame.K_LEFT:
					self.turn(LEFT)
				elif event.key == pygame.K_RIGHT:
					self.turn(RIGHT)





class Food(object):
	def __init__(self):
		self.position = (0,0)
		self.color = (223, 163, 49)
		self.random_tha_pos()

	def random_tha_pos(self):
		self.position = (random.randint(0, GRID_WIDTH-1) * GRIDSIZE, random.randint(0, GRID_HEIGHT-1) * GRIDSIZE)

	def draw(self, surface):
		r = pygame.Rect((self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
		pygame.draw.rect(surface, self.color, r)
		pygame.draw.rect(surface, (93, 216, 228), r, 1)




def drawGrid(surface):
	for y in range(0, int(GRID_HEIGHT)):
		for x in range(0, int(GRID_WIDTH)):
			if (x + y) % 2 == 0:
				r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
				pygame.draw.rect(surface, (93, 216, 228), r)
			else:
				rr = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
				pygame.draw.rect(surface, (84, 194, 205), rr)




SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480

GRIDSIZE = 60
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE

# U kojim se smjerovima zmija moze kretati
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def main():
	pygame.init()

	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32) #32 je koliko bitova koristim za reprezentiranje boje

	surface = pygame.Surface(screen.get_size())
	surface = surface.convert()
	drawGrid(surface)

	snake = Snake()
	food = Food()

	myfont = pygame.font.SysFont("monospace", 16)

	while True:
		clock.tick(8)
		snake.handle_keys()
		drawGrid(surface)
		snake.move()
		if snake.get_head_pos() == food.position:
			snake.lenght += 1
			snake.score += 1
			food.random_tha_pos()
		snake.draw(surface)
		food.draw(surface)
		# handle events
		screen.blit(surface, (0,0))
		text = myfont.render(" Score {0}".format(snake.score), 1, (0,0,0))
		screen.blit(text, (5,10))
		pygame.display.update()

main()