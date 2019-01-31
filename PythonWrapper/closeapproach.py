"""
JPL Close Approach Python Wrapper
Ryan Phillips - 2/1/19

This file wraps the Close Approach API

Usage:
	CloseApproach(**kwargs)
		- get pandas dataframes
		- get json results
	
	see https://ssd-api.jpl.nasa.gov/doc/cad.html
	for a list of possible kwargs to be passed or
	see Examples/examples.py

This is the main class used to call the api and recieve data
for the visual representation

"""
import requests
import pandas as pd
from wrapper_errors import ParameterError



def compute_t_sigma(t_sigma):
	"""
	T sigma is a str consisting of time-stamps
	1_2:15 -> 1 hour, 2 mins, and 15 secs
	rtype: int -> t_sigma in seconds only
	"""
	pass


class CloseApproach(object):

	def __init__(self, **kwargs):

		params = {}

		for k, v in kwargs.items():

			if isinstance(v, dict):

				for k_, v_ in v.items():

					params[k_] = v_
			else:

				params[k] = v

		self.params = params if params else None

		self.endpoint = 'https://ssd-api.jpl.nasa.gov/cad.api'

		self.session = requests.Session()


	def get_json(self, params = None):

		if params is not None:

			if isinstance(params, dict):

				self.params = params

		response = self.session.get(self.endpoint, params=self.params)

		if not response.ok:

			raise ParameterError('Invalid Paramter(s) for API request')

		return response.json()


	def get_frame(self, params = None):

		data = self.get_json(params)

		if data['count'] == '0':

			return None

		d_frame = pd.DataFrame(data['data'], columns=data['fields'])

		for col in d_frame.columns:

			d_frame[col] = pd.to_numeric(d_frame[col], errors='ignore')

		return d_frame


	def scale_for_visualizer(self, epsilon):
		"""Scale might be alright considering AU's"""

		pass


	def __str__(self):

		return '{}'.format(self.get_frame())

	def __repr__(self):

		return '<Close Approach Object> {}'.format(self.endpoint)











