from ursina import *

# BG = background
class BG(Entity):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'quad',
			scale = (0.56,0.86),
			color = color.gray)

class Item(Draggable):
	def __init__(self):
		super().__init__(
			parent = camera.ui,
			model = 'quad', 
			color = color.red,
			scale = (0.1, 0.1))

app = Ursina()
bg = BG()
item = Item()
app.run()