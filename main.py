import pygame
from pygame.locals import *

class App:
	def __init__(self):
		self.running = True
		self.display_surf = None
		self.size = self.weight, self.height = 640, 400

	def on_init(self):
		pygame.init()

		logo = pygame.image.load("assets/chess/white_rook.png")
		pygame.display.set_icon(logo)
		pygame.display.set_caption("chess")
		self.display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)

		self.running = True

		return True
	
	def on_event(self, event):
		if event.type == pygame.QUIT:
			self.running = False

	def on_loop(self):
		pass

	def on_render(self):
		pass

	def on_cleanup(self):
		pygame.quit()

	def on_execute(self):
		if not self.on_init(): #TODO: understand how this works
			self.running = False

		while self.running:
			for event in pygame.event.get():
				self.on_event(event)

			self.on_loop()
			self.on_render()

		self.on_cleanup()

if __name__ == "__main__":
	app = App()
	app.on_execute()
