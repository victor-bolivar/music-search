import requests
import json
import time

# retrieves related songs sorted by ratings/popularity

def timer(function):
	def wrapped(*args):
		start_time = time.time()
		returned_value = function()
		print('function : ({}) , execution time : {}s' .format(function.__name__, time.time()-start_time))
		return returned_value
	return wrapped

@timer
class ItunesInformation():
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