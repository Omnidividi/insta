from config import config
from selenium.webdriver.common.keys import Keys

class Caption:

	def __init__(self, databaseRecord):
		self.record = databaseRecord

	def generate(self):
		genericComponent = self.genericComponent()
		creditComponent = self.creditComponent()
		hashtagComponent = self.hashtagComponent()
		caption = self.combine(genericComponent, creditComponent, hashtagComponent)
		return caption

	def genericComponent(self):
		# find a way to return generic phrases like "beautiful"
		return "via"

	def creditComponent(self):
		userPostWasScrapedFrom = self.record["owner_username"]
		return "@" + userPostWasScrapedFrom

	def hashtagComponent(self):
		hashtags = config.post_hashtag
		hashtagString = ""
		for hashtag in hashtags:
			hashtagString = hashtagString + "#" + hashtag + " "

		print("hashtag string: " + hashtagString)
		return hashtagString

	def combine(self, generic, credit, hashtag):
		caption = "{} {} \n\n.\n.\n.\n{}".format(generic, credit, hashtag)
		caption = caption.replace("\n", Keys.RETURN);
		return caption