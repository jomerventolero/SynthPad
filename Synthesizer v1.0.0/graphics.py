import pygame as pg
from settings import *

class Pad:
    def __init__(self, screen, graphics, x, y):
        screen.blit(graphics, (TILESIZE * x, TILESIZE * y))


class SPad:
	def __init__(self, screen, graphics, x, y, size=[0.5,0.5]):
		self.sizex = size[0]
		self.sizey = size[1]
		self.x = (TILESIZE*self.sizex) * x
		self.y = (TILESIZE*self.sizey) * y
		screen.blit(graphics, (self.x, self.y))

	def move(self, x, y):
		self.x = (TILESIZE*size) * x
		self.y = (TILESIZE*size) * y

	def get_pos(self):
		return (self.x, self.y)

	def get_size(self):
		return (TILESIZE*self.sizex, TILESIZE*self.sizey)


class ExactPad:
	def __init__(self, screen, graphics, x, y):
		screen.blit(graphics, (x, y))
