from config import config
from utilities.logger.MyLogger import MyLogger
import requests

class Request:

	headers = {
		"bot": config.bot_account_id,
		'CONTENT_TYPE': 'application/json',
		'Accept': 'application/json',
	}

	def fullUrl(self, url):
		return config.base_website + url

	def post(self, url, params = {}, data = {}, headers = {}, json={}):
		# define post url
		fullUrl = self.fullUrl(url)
		print("####################### url {} ##################".format(fullUrl))
		# define your URL params (!= of the body of the POST request)
		params = params
		# define the body of the POST request
		data = data
		# send the POST request
		response = requests.post(fullUrl, params=params, data=data, headers=self.headers, json=json)
		if response.status_code != 200:
			self.logFailure(response)

		return response

	def get(self, url, params = {}, headers = {}):
		# define get url
		fullUrl = self.fullUrl(url)
		print("####################### url {} ##################".format(fullUrl))
		# define your URL params
		params = params
		# send the GET request
		response = requests.get(fullUrl, params=params, headers=self.headers)

		if response.status_code != 200:
			self.logFailure(fullUrl, response)
		return response

	def logFailure(self, url, response):
		errorMessage = """
		request sent to: {}
		produced status code: {}
		\n
		{}
		""".format(url, response.status_code, response.text)
		MyLogger().log(errorMessage)