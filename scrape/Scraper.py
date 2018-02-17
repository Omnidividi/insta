from scrape.ScrapeExceptions import ScrapeExceptions
from config import config
from utilities.request.Request import Request

class Scraper:

	def __init__(self, scrapingHandler):
		self.scrapingHandler = scrapingHandler


	def run(self):
		while self.scrapingIncomplete():
			try:
				self.scrapingHandler.run()
			except ScrapeExceptions.NotEnoughPostsFound:
				break
				# LOG: log error to file

	def scrapingIncomplete(self):
		postBacklogAmount = Request().get("/post/backlog/amount").json()
		return postBacklogAmount < config.post_backlog