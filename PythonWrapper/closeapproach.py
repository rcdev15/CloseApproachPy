"""
JPL Close Approach Python Wrapper
Ryan Phillips - 2/1/19

This file wraps the Close Approach API

	CloseApproach(**kwargs)
		- get pandas dataframes
		- get json results
	
see https://ssd-api.jpl.nasa.gov/doc/cad.html for full query info

"""
import requests
import pandas as pd
from wrapper_errors import ParameterError



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



def t_sigma_to_list(t_sigma):
	"""
	Params: str -> 3 sigma uncertainty
	1_2::15 -> 1 day, 2 hours, and 15 mins
	rtype: list -> [days, hours, mins]
	"""
	times = []

	for i in range(len(t_sigma)):

		temp = ''

		if t_sigma[i].isdigit():

			temp += t_sigma[i]

			for j in range(i+1, len(t_sigma)):

				if t_sigma[j].isdigit():

					temp += t_sigma[j]

				else:

					break

		if temp:

			times.append(float(temp))

	return t_sigma_to_hours(times)


def t_sigma_to_hours(time_list):
	"""
	Param: list -> [days, hours, mins]
	rtype: float -> time in only hours
	"""
	if len(time_list) == 3:

		return ((time_list[0] * 24) + time_list[1] + (time_list[2] / 24))

	elif len(time_list) == 2:

		return (time_list[0] + (time_list[1] / 24))

	elif len(time_list) == 1:

		return (time_list[0] / 24)

	else:

		return None

