
from vpython import *
from math import sin, cos


class Planet(object):

	def __init__(self, radius, s_pos, material = None, color = None):

		if color is None:

			self.celestial = vpython.sphere()

		elif material is None:

			pass

		else:

			pass
