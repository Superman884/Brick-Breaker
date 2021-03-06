import pygame
import colorsys
from random import randrange
import keyboard
from time import sleep
pygame.init()
class ball:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.xvel=1
		self.yvel=-1
		self.width=25
		self.height=25
		self.bounce=1
		self.hit=[]
class paddle:
	def __init__(self,x,y,width):
		self.x=x
		self.y=y
		self.width=width
		self.height=26
class block:
	def __init__(self,x,y,hp):
		self.x=x
		self.y=y
		self.width=wid
		self.height=hei
		self.hp=hp
def collide(ball1,pad,old,top,xv,yv):
	global blocks
	if (pad.x,pad.y) in ball1.hit and not top:
		return ball1
	if top:
		if (ball1.y<pad.y and ball1.y+ball1.height>pad.y) or (ball1.y<pad.y+pad.height and ball1.y+ball1.height>pad.y+pad.height):
			if ball1.x<old and ball1.x+ball1.width>pad.x:
				ball1.xvel=-1
				if not top:
					try:
						pad.hp-=1
						if pad.hp==0:
							blocks.pop(blocks.index(pad))
						ball1.bounce+=0.1
					except:
						pass
				else:
					ball1.bounce+=0.1
			elif ball1.x<old+pad.width and ball1.x+ball1.width>pad.x+pad.width:
				ball1.xvel=1
				if not top:
					try:
						pad.hp-=1
						if pad.hp==0:
							blocks.pop(blocks.index(pad))
						ball1.bounce+=0.1
					except:
						pass
				else:
					ball1.bounce+=0.1
	else:
		if (ball1.y<pad.y and ball1.y+ball1.height>pad.y) or (ball1.y<pad.y+pad.height and ball1.y+ball1.height>pad.y+pad.height):
			if ball1.x+ball1.width==pad.x:
				ball1.xvel=-1
				if not top:
					try:
						pad.hp-=1
						if pad.hp==0:
							blocks.pop(blocks.index(pad))
						ball1.bounce+=0.1
					except:
						pass
				else:
					ball1.bounce+=0.1
			elif ball1.x==pad.x+pad.width:
				ball1.xvel=1
				if not top:
					try:
						pad.hp-=1
						if pad.hp==0:
							blocks.pop(blocks.index(pad))
						ball1.bounce+=0.1
					except:
						pass
				else:
					ball1.bounce+=0.1
	if ball1.xvel!=xv:
		return ball1
	elif ball1.y<pad.y and ball1.y+ball1.height>pad.y:
		if (ball1.x<pad.x and ball1.x+ball1.width>pad.x) or (ball1.x>pad.x and ball1.x<pad.x+pad.width) or (ball1.x<pad.x+pad.width and ball1.x+ball1.width>pad.x+pad.width):
			ball1.yvel=-1
			ball1.y+=ball1.yvel
			if top:
				ball1.y=pad.y-1-ball1.height
			if not top:
				try:
					pad.hp-=1
					if pad.hp==0:
						blocks.pop(blocks.index(pad))
					ball1.bounce+=0.1
				except:
					pass
			else:
				ball1.bounce+=0.1
	elif ball1.y<pad.y+pad.height and ball1.y+ball1.height>pad.y+pad.height:
		if (ball1.x<pad.x and ball1.x+ball1.width>pad.x) or (ball1.x>pad.x and ball1.x<pad.x+pad.width) or (ball1.x<pad.x+pad.width and ball1.x+ball1.width>pad.x+pad.width):
			ball1.yvel=1
			ball1.y+=ball1.yvel
			if top:
				ball1.y=pad.y-1-ball1.height
			if not top:
				try:
					pad.hp-=1
					if pad.hp==0:
						blocks.pop(blocks.index(pad))
					ball1.bounce+=0.1
				except:
					pass
			else:
				ball1.bounce+=0.1
	if xv!=ball1.xvel or yv!=ball1.yvel:
		ball1.hit.append((pad.x,pad.y))
	return ball1
wid=50
hei=25
ball_img=pygame.image.load('ball.png')
pad_img=pygame.image.load('paddle.png')
rule={1:(20,200,20),2:(206,206,0),3:(153,217,232)
,4:(0,64,128),5:(128,0,128)}
block_imgs=[]
dell=0
for i in range(1,6):
	rock=pygame.Surface((wid,hei))
	pock=pygame.Surface((wid-8,hei-8))
	point=rule[i]
	pointv=colorsys.rgb_to_hls(point[0]/256,point[1]/256,point[2]/256)
	new=(pointv[0],pointv[1]/2,pointv[2])
	new=colorsys.hls_to_rgb(new[0],new[1],new[2])
	new=(new[0]*256,new[1]*256,new[2]*256)
	rock.fill(new)
	pock.fill(rule[i])
	rock.blit(pock,(4,4))
	block_imgs.append(rock)
win=pygame.display.set_mode((1000,500))
run=True
ball1=ball(700,400)
bad_blocks=[]
level=1
lives=3
if level==3:
	bad_blocks=[(150, 0, 2), (150, 25, 1), (150, 50, 2), (150, 75, 1), (150, 100, 2), (150, 125, 1), (250, 150, 1), (250, 175, 2), (250, 200, 1), (250, 225, 2), (250, 250, 1), (250, 275, 2), (200, 250, 1), (150, 250, 1), (100, 250, 1), (50, 250, 1), (0, 250, 1), (0, 275, 2), (50, 275, 2), (100, 275, 2), (150, 275, 2), (200, 275, 2), (300, 150, 2), (350, 150, 1), (300, 175, 2), (300, 200, 2), (300, 225, 2), (300, 250, 2), (300, 275, 2), (350, 175, 2), (350, 200, 1), (350, 225, 2), (350, 250, 1), (350, 275, 2), (400, 250, 2), (450, 250, 1), (500, 250, 3), (550, 250, 1), (600, 250, 2), (650, 250, 1), (700, 250, 2), (750, 250, 1), (800, 250, 1), (850, 250, 1), (900, 250, 1), (950, 250, 1), (950, 275, 2), (850, 275, 2), (900, 275, 2), (800, 275, 2), (750, 275, 2), (700, 275, 2), (600, 275, 2), (650, 275, 2), (550, 275, 2), (500, 275, 2), (450, 275, 2), (400, 275, 2), (400, 150, 2), (400, 175, 2), (400, 200, 2), (400, 225, 2), (450, 150, 1), (450, 175, 2), (450, 200, 1), (450, 225, 2), (800, 0, 2), (800, 25, 1), (800, 50, 2), (800, 75, 1), (800, 100, 2), (800, 125, 1), (700, 150, 2), (700, 175, 2), (700, 200, 2), (700, 225, 2), (650, 225, 2), (600, 225, 2), (550, 225, 2), (500, 225, 3), (500, 200, 3), (500, 175, 3), (500, 150, 3), (550, 150, 1), (600, 150, 2), (650, 150, 1), (650, 175, 2), (600, 175, 2), (550, 175, 2), (550, 200, 1), (600, 200, 2), (650, 200, 1)]
if level==1:
	bad_blocks=[(200, 50, 1), (150, 75, 1), (150, 150, 1), (150, 175, 1), (150, 250, 1), (200, 275, 1), (350, 300, 1), (400, 300, 1), (300, 300, 1), (500, 275, 1), (550, 250, 1), (550, 175, 1), (550, 150, 1), (550, 75, 1), (500, 50, 1), (300, 0, 1), (350, 0, 1), (400, 0, 1), (350, 150, 2)]
if level==2:
	bad_blocks=[(450, 50, 1), (450, 100, 1), (450, 75, 1), (450, 125, 1), (450, 150, 1), (450, 175, 1), (450, 200, 1), (450, 225, 1), (400, 75, 2), (400, 100, 2), (400, 125, 2), (400, 150, 2), (400, 175, 2), (400, 200, 2), (500, 200, 2), (500, 175, 2), (500, 150, 2), (500, 100, 2), (500, 125, 2), (500, 50, 2), (500, 75, 2), (400, 50, 2), (450, 25, 1), (450, 250, 1), (450, 275, 1), (400, 225, 2), (400, 250, 2), (500, 225, 2), (500, 250, 2), (350, 75, 1), (350, 100, 1), (350, 125, 1), (350, 150, 1), (350, 175, 1), (350, 200, 1), (350, 225, 1), (550, 75, 1), (550, 100, 1), (550, 150, 1), (550, 125, 1), (550, 175, 1), (550, 200, 1), (550, 225, 1), (300, 100, 2), (300, 125, 2), (300, 150, 2), (300, 175, 2), (300, 200, 2), (250, 125, 1), (250, 150, 1), (250, 175, 1), (200, 150, 3), (600, 100, 2), (600, 125, 2), (600, 150, 2), (600, 175, 2), (600, 200, 2), (650, 125, 1), (650, 150, 1), (650, 175, 1), (700, 150, 3)]
if level==4:
	bad_blocks=[(50, 0, 5), (50, 25, 5), (50, 50, 5), (50, 75, 5), (50, 100, 5), (50, 125, 5), (50, 150, 5), (50, 175, 5), (50, 200, 5), (50, 225, 5), (100, 225, 5), (150, 225, 5), (200, 225, 5), (250, 225, 5), (300, 225, 5), (300, 200, 5), (300, 175, 5), (300, 150, 5), (300, 125, 5), (300, 100, 5), (300, 75, 5), (300, 50, 5), (300, 25, 5), (300, 0, 5), (650, 225, 5), (600, 225, 5), (700, 225, 5), (750, 225, 5), (800, 225, 5), (850, 225, 5), (600, 200, 5), (600, 175, 5), (600, 150, 5), (600, 125, 5), (600, 100, 5), (600, 75, 5), (600, 50, 5), (600, 25, 5), (600, 0, 5), (850, 200, 5), (850, 175, 5), (850, 150, 5), (850, 125, 5), (850, 100, 5), (850, 75, 5), (850, 50, 5), (850, 25, 5), (850, 0, 5), (100, 0, 4), (150, 0, 4), (200, 0, 4), (250, 0, 4), (650, 25, 4), (650, 0, 4), (700, 0, 4), (750, 0, 4), (800, 0, 4), (100, 25, 4), (100, 50, 4), (100, 75, 4), (650, 50, 4), (650, 75, 4), (250, 50, 4), (250, 25, 4), (250, 75, 4), (100, 100, 3), (100, 125, 3), (100, 150, 3), (100, 175, 5), (100, 200, 4), (150, 200, 4), (200, 200, 4), (250, 200, 4), (150, 175, 5), (200, 175, 5), (250, 175, 5), (650, 175, 5), (700, 175, 5), (750, 175, 5), (800, 175, 5), (650, 200, 4), (700, 200, 4), (800, 200, 4), (750, 200, 4), (800, 25, 4), (800, 50, 4), (800, 75, 4), (650, 100, 3), (650, 125, 3), (650, 150, 3), (800, 100, 3), (800, 125, 3), (800, 150, 3), (250, 100, 3), (250, 125, 3), (250, 150, 3), (150, 125, 2), (200, 125, 2), (700, 125, 2), (750, 125, 2), (150, 50, 3), (200, 50, 3), (700, 50, 3), (750, 50, 3)]
if level==5:
	bad_blocks=[(0, 0, 5), (50, 0, 5), (100, 0, 5), (150, 0, 5), (200, 0, 5), (250, 0, 5), (350, 0, 5), (300, 0, 5), (400, 0, 5), (450, 0, 5), (500, 0, 5), (600, 0, 5), (550, 0, 5), (650, 0, 5), (700, 0, 5), (750, 0, 5), (800, 0, 5), (900, 0, 5), (850, 0, 5), (950, 0, 5), (0, 25, 5), (50, 25, 5), (100, 25, 5), (200, 25, 5), (150, 25, 5), (250, 25, 5), (300, 25, 5), (350, 25, 5), (350, 50, 4), (400, 25, 5), (450, 25, 5), (500, 25, 5), (550, 25, 5), (600, 25, 5), (650, 25, 5), (700, 25, 5), (750, 25, 5), (800, 25, 5), (750, 50, 4), (850, 25, 5), (900, 25, 5), (950, 25, 5), (0, 50, 5), (50, 50, 4), (100, 50, 4), (150, 50, 4), (200, 50, 4), (250, 50, 4), (300, 50, 4), (400, 50, 4), (450, 50, 4), (500, 50, 5), (550, 50, 4), (600, 50, 4), (650, 75, 4), (650, 50, 4), (700, 50, 4), (800, 50, 4), (850, 50, 4), (900, 50, 4), (950, 50, 5), (950, 75, 5), (900, 75, 4), (850, 75, 4), (800, 75, 4), (750, 75, 4), (700, 75, 4), (600, 75, 4), (550, 75, 4), (500, 75, 5), (450, 75, 4), (400, 75, 4), (350, 75, 4), (300, 75, 4), (250, 75, 4), (200, 75, 4), (150, 75, 4), (100, 75, 4), (50, 75, 4), (0, 75, 5), (0, 150, 5), (50, 150, 3), (100, 150, 3), (150, 150, 3), (200, 150, 3), (250, 150, 4), (300, 150, 3), (350, 150, 3), (400, 150, 3), (450, 150, 3), (500, 150, 5), (600, 150, 3), (550, 150, 3), (650, 150, 3), (750, 150, 3), (700, 150, 3), (800, 150, 3), (850, 150, 4), (900, 150, 3), (950, 150, 5), (0, 175, 5), (50, 175, 3), (100, 175, 3), (200, 175, 3), (150, 175, 3), (300, 175, 3), (250, 175, 4), (350, 175, 3), (400, 175, 3), (450, 175, 3), (500, 175, 5), (550, 175, 3), (600, 175, 3), (700, 175, 3), (650, 175, 3), (800, 175, 3), (750, 175, 3), (850, 175, 4), (900, 175, 3), (950, 175, 5), (0, 225, 5), (50, 225, 2), (0, 250, 5), (50, 250, 2), (0, 275, 5), (0, 300, 5), (50, 300, 1), (50, 275, 1), (100, 225, 2), (100, 250, 2), (100, 275, 1), (100, 300, 1), (150, 300, 1), (200, 300, 1), (250, 300, 4), (350, 300, 1), (300, 300, 1), (400, 300, 1), (500, 300, 5), (450, 300, 1), (550, 300, 1), (600, 300, 1), (650, 300, 1), (700, 300, 1), (750, 300, 1), (800, 300, 1), (850, 300, 4), (900, 300, 1), (950, 300, 5), (950, 275, 5), (950, 250, 5), (950, 225, 5), (900, 225, 2), (850, 225, 4), (800, 225, 2), (750, 225, 2), (700, 225, 2), (600, 225, 2), (650, 225, 2), (550, 225, 2), (500, 225, 5), (450, 225, 2), (400, 225, 2), (350, 225, 2), (300, 225, 2), (250, 225, 4), (200, 225, 2), (150, 225, 2), (150, 250, 2), (150, 275, 1), (200, 250, 2), (200, 275, 1), (250, 250, 4), (300, 250, 2), (350, 250, 2), (400, 250, 2), (450, 250, 2), (250, 275, 4), (300, 275, 1), (350, 275, 1), (400, 275, 1), (450, 275, 1), (500, 250, 5), (500, 275, 5), (550, 275, 1), (550, 250, 2), (600, 250, 2), (600, 275, 1), (650, 275, 1), (650, 250, 2), (700, 250, 2), (700, 275, 1), (750, 275, 1), (750, 250, 2), (800, 250, 2), (800, 275, 1), (850, 275, 4), (850, 250, 4), (900, 250, 2), (900, 275, 1), (250, 200, 4), (250, 125, 4), (250, 100, 4), (850, 200, 4), (850, 125, 4), (850, 100, 4), (500, 100, 5), (500, 125, 5), (550, 125, 5), (550, 100, 5), (500, 200, 5), (550, 200, 5), (450, 100, 5), (450, 125, 5), (450, 200, 5), (0, 100, 5), (0, 125, 5), (50, 200, 3), (0, 200, 5), (100, 200, 3), (150, 200, 3), (200, 200, 3), (300, 200, 3), (350, 200, 3), (400, 200, 3), (600, 200, 3), (650, 200, 3), (700, 200, 3), (750, 200, 3), (800, 200, 3), (900, 200, 3), (950, 200, 5), (950, 125, 5), (950, 100, 5)]
# for y in range(1,11):
# 	for x in range(1000//50):
# 		bad_blocks.append((x,y,5-((y-1)//2)))
blocks=[]
pad=paddle(700,400,132)
pause=False
start=True
for i in bad_blocks:
	a=block(i[0],i[1],i[2])
	blocks.append(a)
while run:
	if pause:
		sleep(3)
		pause=False
	if len(blocks)==0:
		level+=1
		if level==3:
			bad_blocks=[(150, 0, 2), (150, 25, 1), (150, 50, 2), (150, 75, 1), (150, 100, 2), (150, 125, 1), (250, 150, 1), (250, 175, 2), (250, 200, 1), (250, 225, 2), (250, 250, 1), (250, 275, 2), (200, 250, 1), (150, 250, 1), (100, 250, 1), (50, 250, 1), (0, 250, 1), (0, 275, 2), (50, 275, 2), (100, 275, 2), (150, 275, 2), (200, 275, 2), (300, 150, 2), (350, 150, 1), (300, 175, 2), (300, 200, 2), (300, 225, 2), (300, 250, 2), (300, 275, 2), (350, 175, 2), (350, 200, 1), (350, 225, 2), (350, 250, 1), (350, 275, 2), (400, 250, 2), (450, 250, 1), (500, 250, 3), (550, 250, 1), (600, 250, 2), (650, 250, 1), (700, 250, 2), (750, 250, 1), (800, 250, 1), (850, 250, 1), (900, 250, 1), (950, 250, 1), (950, 275, 2), (850, 275, 2), (900, 275, 2), (800, 275, 2), (750, 275, 2), (700, 275, 2), (600, 275, 2), (650, 275, 2), (550, 275, 2), (500, 275, 2), (450, 275, 2), (400, 275, 2), (400, 150, 2), (400, 175, 2), (400, 200, 2), (400, 225, 2), (450, 150, 1), (450, 175, 2), (450, 200, 1), (450, 225, 2), (800, 0, 2), (800, 25, 1), (800, 50, 2), (800, 75, 1), (800, 100, 2), (800, 125, 1), (700, 150, 2), (700, 175, 2), (700, 200, 2), (700, 225, 2), (650, 225, 2), (600, 225, 2), (550, 225, 2), (500, 225, 3), (500, 200, 3), (500, 175, 3), (500, 150, 3), (550, 150, 1), (600, 150, 2), (650, 150, 1), (650, 175, 2), (600, 175, 2), (550, 175, 2), (550, 200, 1), (600, 200, 2), (650, 200, 1)]
		if level==1:
			bad_blocks=[(200, 50, 1), (150, 75, 1), (150, 150, 1), (150, 175, 1), (150, 250, 1), (200, 275, 1), (350, 300, 1), (400, 300, 1), (300, 300, 1), (500, 275, 1), (550, 250, 1), (550, 175, 1), (550, 150, 1), (550, 75, 1), (500, 50, 1), (300, 0, 1), (350, 0, 1), (400, 0, 1), (350, 150, 2)]
		if level==2:
			bad_blocks=[(450, 50, 1), (450, 100, 1), (450, 75, 1), (450, 125, 1), (450, 150, 1), (450, 175, 1), (450, 200, 1), (450, 225, 1), (400, 75, 2), (400, 100, 2), (400, 125, 2), (400, 150, 2), (400, 175, 2), (400, 200, 2), (500, 200, 2), (500, 175, 2), (500, 150, 2), (500, 100, 2), (500, 125, 2), (500, 50, 2), (500, 75, 2), (400, 50, 2), (450, 25, 1), (450, 250, 1), (450, 275, 1), (400, 225, 2), (400, 250, 2), (500, 225, 2), (500, 250, 2), (350, 75, 1), (350, 100, 1), (350, 125, 1), (350, 150, 1), (350, 175, 1), (350, 200, 1), (350, 225, 1), (550, 75, 1), (550, 100, 1), (550, 150, 1), (550, 125, 1), (550, 175, 1), (550, 200, 1), (550, 225, 1), (300, 100, 2), (300, 125, 2), (300, 150, 2), (300, 175, 2), (300, 200, 2), (250, 125, 1), (250, 150, 1), (250, 175, 1), (200, 150, 3), (600, 100, 2), (600, 125, 2), (600, 150, 2), (600, 175, 2), (600, 200, 2), (650, 125, 1), (650, 150, 1), (650, 175, 1), (700, 150, 3)]
		if level==4:
			bad_blocks=[(50, 0, 5), (50, 25, 5), (50, 50, 5), (50, 75, 5), (50, 100, 5), (50, 125, 5), (50, 150, 5), (50, 175, 5), (50, 200, 5), (50, 225, 5), (100, 225, 5), (150, 225, 5), (200, 225, 5), (250, 225, 5), (300, 225, 5), (300, 200, 5), (300, 175, 5), (300, 150, 5), (300, 125, 5), (300, 100, 5), (300, 75, 5), (300, 50, 5), (300, 25, 5), (300, 0, 5), (650, 225, 5), (600, 225, 5), (700, 225, 5), (750, 225, 5), (800, 225, 5), (850, 225, 5), (600, 200, 5), (600, 175, 5), (600, 150, 5), (600, 125, 5), (600, 100, 5), (600, 75, 5), (600, 50, 5), (600, 25, 5), (600, 0, 5), (850, 200, 5), (850, 175, 5), (850, 150, 5), (850, 125, 5), (850, 100, 5), (850, 75, 5), (850, 50, 5), (850, 25, 5), (850, 0, 5), (100, 0, 4), (150, 0, 4), (200, 0, 4), (250, 0, 4), (650, 25, 4), (650, 0, 4), (700, 0, 4), (750, 0, 4), (800, 0, 4), (100, 25, 4), (100, 50, 4), (100, 75, 4), (650, 50, 4), (650, 75, 4), (250, 50, 4), (250, 25, 4), (250, 75, 4), (100, 100, 3), (100, 125, 3), (100, 150, 3), (100, 175, 5), (100, 200, 4), (150, 200, 4), (200, 200, 4), (250, 200, 4), (150, 175, 5), (200, 175, 5), (250, 175, 5), (650, 175, 5), (700, 175, 5), (750, 175, 5), (800, 175, 5), (650, 200, 4), (700, 200, 4), (800, 200, 4), (750, 200, 4), (800, 25, 4), (800, 50, 4), (800, 75, 4), (650, 100, 3), (650, 125, 3), (650, 150, 3), (800, 100, 3), (800, 125, 3), (800, 150, 3), (250, 100, 3), (250, 125, 3), (250, 150, 3), (150, 125, 2), (200, 125, 2), (700, 125, 2), (750, 125, 2), (150, 50, 3), (200, 50, 3), (700, 50, 3), (750, 50, 3)]
		if level==5:
			bad_blocks=[(0, 0, 5), (50, 0, 5), (100, 0, 5), (150, 0, 5), (200, 0, 5), (250, 0, 5), (350, 0, 5), (300, 0, 5), (400, 0, 5), (450, 0, 5), (500, 0, 5), (600, 0, 5), (550, 0, 5), (650, 0, 5), (700, 0, 5), (750, 0, 5), (800, 0, 5), (900, 0, 5), (850, 0, 5), (950, 0, 5), (0, 25, 5), (50, 25, 5), (100, 25, 5), (200, 25, 5), (150, 25, 5), (250, 25, 5), (300, 25, 5), (350, 25, 5), (350, 50, 4), (400, 25, 5), (450, 25, 5), (500, 25, 5), (550, 25, 5), (600, 25, 5), (650, 25, 5), (700, 25, 5), (750, 25, 5), (800, 25, 5), (750, 50, 4), (850, 25, 5), (900, 25, 5), (950, 25, 5), (0, 50, 5), (50, 50, 4), (100, 50, 4), (150, 50, 4), (200, 50, 4), (250, 50, 4), (300, 50, 4), (400, 50, 4), (450, 50, 4), (500, 50, 5), (550, 50, 4), (600, 50, 4), (650, 75, 4), (650, 50, 4), (700, 50, 4), (800, 50, 4), (850, 50, 4), (900, 50, 4), (950, 50, 5), (950, 75, 5), (900, 75, 4), (850, 75, 4), (800, 75, 4), (750, 75, 4), (700, 75, 4), (600, 75, 4), (550, 75, 4), (500, 75, 5), (450, 75, 4), (400, 75, 4), (350, 75, 4), (300, 75, 4), (250, 75, 4), (200, 75, 4), (150, 75, 4), (100, 75, 4), (50, 75, 4), (0, 75, 5), (0, 150, 5), (50, 150, 3), (100, 150, 3), (150, 150, 3), (200, 150, 3), (250, 150, 4), (300, 150, 3), (350, 150, 3), (400, 150, 3), (450, 150, 3), (500, 150, 5), (600, 150, 3), (550, 150, 3), (650, 150, 3), (750, 150, 3), (700, 150, 3), (800, 150, 3), (850, 150, 4), (900, 150, 3), (950, 150, 5), (0, 175, 5), (50, 175, 3), (100, 175, 3), (200, 175, 3), (150, 175, 3), (300, 175, 3), (250, 175, 4), (350, 175, 3), (400, 175, 3), (450, 175, 3), (500, 175, 5), (550, 175, 3), (600, 175, 3), (700, 175, 3), (650, 175, 3), (800, 175, 3), (750, 175, 3), (850, 175, 4), (900, 175, 3), (950, 175, 5), (0, 225, 5), (50, 225, 2), (0, 250, 5), (50, 250, 2), (0, 275, 5), (0, 300, 5), (50, 300, 1), (50, 275, 1), (100, 225, 2), (100, 250, 2), (100, 275, 1), (100, 300, 1), (150, 300, 1), (200, 300, 1), (250, 300, 4), (350, 300, 1), (300, 300, 1), (400, 300, 1), (500, 300, 5), (450, 300, 1), (550, 300, 1), (600, 300, 1), (650, 300, 1), (700, 300, 1), (750, 300, 1), (800, 300, 1), (850, 300, 4), (900, 300, 1), (950, 300, 5), (950, 275, 5), (950, 250, 5), (950, 225, 5), (900, 225, 2), (850, 225, 4), (800, 225, 2), (750, 225, 2), (700, 225, 2), (600, 225, 2), (650, 225, 2), (550, 225, 2), (500, 225, 5), (450, 225, 2), (400, 225, 2), (350, 225, 2), (300, 225, 2), (250, 225, 4), (200, 225, 2), (150, 225, 2), (150, 250, 2), (150, 275, 1), (200, 250, 2), (200, 275, 1), (250, 250, 4), (300, 250, 2), (350, 250, 2), (400, 250, 2), (450, 250, 2), (250, 275, 4), (300, 275, 1), (350, 275, 1), (400, 275, 1), (450, 275, 1), (500, 250, 5), (500, 275, 5), (550, 275, 1), (550, 250, 2), (600, 250, 2), (600, 275, 1), (650, 275, 1), (650, 250, 2), (700, 250, 2), (700, 275, 1), (750, 275, 1), (750, 250, 2), (800, 250, 2), (800, 275, 1), (850, 275, 4), (850, 250, 4), (900, 250, 2), (900, 275, 1), (250, 200, 4), (250, 125, 4), (250, 100, 4), (850, 200, 4), (850, 125, 4), (850, 100, 4), (500, 100, 5), (500, 125, 5), (550, 125, 5), (550, 100, 5), (500, 200, 5), (550, 200, 5), (450, 100, 5), (450, 125, 5), (450, 200, 5), (0, 100, 5), (0, 125, 5), (50, 200, 3), (0, 200, 5), (100, 200, 3), (150, 200, 3), (200, 200, 3), (300, 200, 3), (350, 200, 3), (400, 200, 3), (600, 200, 3), (650, 200, 3), (700, 200, 3), (750, 200, 3), (800, 200, 3), (900, 200, 3), (950, 200, 5), (950, 125, 5), (950, 100, 5)]
		for i in bad_blocks:
			a=block(i[0],i[1],i[2])
			blocks.append(a)
		lives=8
		ball1=ball(pad.x-20,pad.y-50)
		pause=True
	if ball1.y>500 and lives!=0:
		lives-=1
		ball1=ball(pad.x+25,400)
	if keyboard.is_pressed('q'):
		run=False
	if keyboard.is_pressed('p') and dell==0:
		bad_blocks.pop(-1)
		dell=500
	if dell!=0:
		dell-=1
	old=pad.x
	win.fill((0,0,0))
	win.blit(ball_img,(ball1.x,ball1.y))
	win.blit(pad_img,(pad.x,pad.y))
	for i in blocks:
		win.blit(block_imgs[i.hp-1],(i.x,i.y))
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
		if event.type==pygame.MOUSEBUTTONDOWN and False:
			pos = pygame.mouse.get_pos()
			bad_blocks.append((pos[0]//wid,pos[1]//hei,1))
			blocks=[]
			for i in bad_blocks:
				a=block(i[0]*wid,i[1]*hei,i[2])
				mom=True
				for j in blocks:
					if a.x==j.x and a.y==j.y :
						if j.hp!=5:
							blocks[blocks.index(j)].hp+=1
						mom=False
						break
				if mom:
					blocks.append(a)
			print(len(blocks))
	pygame.display.update()
	ball1.x+=(ball1.xvel)#*ball1.bounce)/2
	ball1.y+=(ball1.yvel)#*ball1.bounce)/2
	pos = pygame.mouse.get_pos()[0]
	pad.x=pos-pad.width/2
	if start:
		ball1.x=pad.x-25
		start=False
	if pad.x+pad.width>1000:
		pad.x=1000-pad.width
	if pad.x<0:
		pad.x=0
	if ball1.x<0 or ball1.x+ball1.width>1000:
		ball1.xvel*=-1
		ball1.x+=ball1.xvel
		ball1.bounce+=0.1
	if ball1.y<=0:
		ball1.yvel*=-1
		ball1.y+=1
		ball1.bounce+=0.1
	pp=ball1.xvel
	mm=ball1.yvel
	ball1=collide(ball1,pad,old,True,pp,mm)
	pp=ball1.xvel
	mm=ball1.yvel
	ball1.hit=[]
	for i in blocks:
		ball1=collide(ball1,i,i.x,False,pp,mm)
boo=[]
for i in blocks:
	pp=(i.x,i.y,i.hp)
	boo.append(pp)