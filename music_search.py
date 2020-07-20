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


class ItunesInformation:
	def __init__(self, song):
		self.song = song
		self.data = 'NO DATA FOUND'

	def __str__(self):
		return 'object with information for the song : '+self.song.upper()

	def encode(self, string):
		return string.replace(' ', '+')

	@timer
	def get_data(self):
		''''returns a dictionary with the data for 5 results related to
		a given song, which name 'song' must be encoded (i.e. De+Musica+Ligera)'''

		base_url = 'https://itunes.apple.com/search?'
		parameters = {}
		parameters['term'] = self.encode(self.song)
		parameters['country'] = 'US'
		parameters['media'] = 'music'
		parameters['entity'] = 'musicTrack'
		parameters['limit'] = '5'

		res = requests.get(base_url, params=parameters)
		self.data = res.json()

	def data_generator(self):
		for i in range(5):
			yield self.data['results'][i]['trackId'], self.data['results'][i]['trackPrice'], self.data['results'][i]['trackViewUrl']

	def list_results(self):
		''' returns a list of dictionaries with trackId,trackPrice and trackViewUrl'''
		results = [{'trackId':trackId, 'trackPrice':trackPrice, 'trackViewUrl':trackViewUrl} for trackId,trackPrice,trackViewUrl in self.data_generator()]
		results = sorted(results, key=lambda result : float(result['trackPrice']), reverse=True)
		return results

if __name__ == '__main__':

	iTunes = ItunesInformation('de musica ligera')
	iTunes.get_data()
	print(iTunes.list_results())