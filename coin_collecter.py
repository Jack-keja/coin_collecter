# game description:The flower will show randomly on the screen, you need to click it and get score, if you miss, the game will stop and tell you the score.
import pgzrun
from random import randint

WIDTH = 300
HEIGHT = 300 # set the screen side
score = 0 # set the score

coin= Actor("coin")

def draw(): # draw the flower on the screen
	screen.fill("white")  # fill the background
	coin.draw()

def on_mouse_down(pos): # check if the mouse click the flower
	global score
	if(coin.collidepoint(pos)):
		score = score +1 # if click, add 1 score
		place() 
	else:
		print("score is " , score) # not click, output the score, quit.
		quit()
		
def place(): # randomly move the flower
	coin.x = randint(10,WIDTH)
	coin.y = randint(10,HEIGHT)

pgzrun.go() # start the game