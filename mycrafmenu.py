from ursina import *

# BG = background
class BG(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'quad',
			scale = (0.56,0.86),
			color = color.gray)

app = Ursina()
bg = BG()
app.run()