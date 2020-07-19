import requests
import json

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