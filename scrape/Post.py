from time import sleep
from config import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from utilities.filedriver.Local import Local
from scrape.ScrapeExceptions import ScrapeExceptions
from utilities.request.Request import Request
import datetime

class Post:

	def __init__(self, postUrl, browser):
		self.postUrl = postUrl
		self.instaId = self.postUrl.split("/p/")[1].replace("/", "")
		self.browser = browser

	def scrape(self):
		try: 
			self.savePost() 
		except ScrapeExceptions.FileSaveError:
			# post could not be saved
			# delete database record
			# scrape for another post
			print("post could not be saved")
		except ScrapeExceptions.DatabaseError:
			# post could not be inserted into database
			print("post could not be inserted into database")

	## Checking Eligibility
	def eligibleForScraping(self):
		self.browser.get(self.postUrl)

		# check is it is a video
		if self.postIsAVideo():
			print("post is a video")
			return False

		self.imageUrl = self.browser.find_element_by_css_selector("img._2di5p").get_attribute("src")
		sleep(3)
		
		# not on hashtag blacklist
		if self.postIsOnHashtagBlacklist():
			print("post is on hashtag blacklist")
			return False

		# not in database (id/url)
		if self.postIsAlreadyInDatabase():
			print("post is already in database")
			return False

		return True

	def postIsAVideo(self):
		try:
			self.browser.find_element_by_css_selector("a._v7u5u._pqxoc._75c7w.videoSpritePlayButton")
			return True
		except:
			return False

		return True

	def postIsOnHashtagBlacklist(self):
		blacklistedHashtags = config.hashtag_blacklist
		thisPostHashtagLinks = self.browser.find_elements_by_partial_link_text('#')
		thisPostHashtags = list(map(lambda link: link.text.replace("#", ""), thisPostHashtagLinks))
		commonHashtags = any(hashtag in blacklistedHashtags for hashtag in thisPostHashtags)
		return commonHashtags

	def postIsAlreadyInDatabase(self):
		parameters = {"insta_id": self.instaId}
		request = Request().post("/post/exists", parameters)

		if request.status_code == 200:
			return request.json() # true or false
		else:
			raise ScrapeExceptions.DatabaseError()



	##
	## Saving Post
	##
	def savePost(self):
		## commit to database
		self.savePostToDatabase()
				
		## saveLocation = s3()
		saveLocation = Local() # maybe extract this to config
		saveLocation.download(self)

			
	def savePostToDatabase(self):
		self.scrapeAttributes()

		parameters = {
			"originally_posted_at": self.originallyPostedAt,
			"scraped_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
			"posted_at": None,
			"insta_id": self.instaId,
			"file_path": self.instaId,
			"instagram_post_url": self.postUrl,
			"instagram_image_url": self.imageUrl,
			"owner_username": self.ownerUserName,
			"original_caption": self.originalCaption,
			"approved": 0,
			"disapproved": 0,
		}
		request = Request().post("/post", parameters)
		print(request)
		print(request.text)
		if request.status_code == 200:
			return True
		else:
			raise ScrapeExceptions.DatabaseError()

		sleep(120)

	def scrapeAttributes(self):
		self.originallyPostedAt = self.browser.find_element_by_css_selector("a._djdmk time._p29ma._6g6t5").get_attribute("datetime")
		self.ownerUserName = self.browser.find_element_by_css_selector("div._74oom div._eeohz a._2g7d5._iadoq").get_attribute("title")
		self.originalCaption = self.browser.find_element_by_css_selector("ul._b0tqa li._ezgzd:first-child").find_element_by_css_selector("span").text





