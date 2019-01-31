
from vpython import sphere, canvas, vector, color, material
from math import sin, cos


class Planet(object):

	def __init__(self, radius, s_pos, material = None, color = None):

		pass




class Star(object):

	def __init__(self, radius, s_pos, color = vpython.colors.yellow):


		pass




class Comet(object):

	def __init__(self, close_approach_object):


		self.data = close_approach_object.get_frame()

		pass
		