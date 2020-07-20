import requests
import json
import time

# retrieves related songs sorted by ratings/popularity

def timer(function):
	def wrapped(*a, **kw):
		start_time = time.time()
		returned_value = function(*a, **kw)
		print('function : ({}) , execution time : {}s' .format(function.__name__, time.time()-start_time))
		return returned_value
	return wrapped


class ItunesInformation():

	@timer
	def get_data(self, song):
		base_url = 'https://itunes.apple.com/search?'
		parameters = {}
		parameters['term'] = song
		parameters['country'] = 'US'

		res =requests.get(base_url, params=parameters)
		print(res.json())

if __name__ == '__main__':

	iTunes = ItunesInformation()
	iTunes.get_data('YMCA')