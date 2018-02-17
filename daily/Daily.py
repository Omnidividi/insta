from utilities.email.EmailDriver import Email
from utilities.email.EmailVariants.EvaluatePosts import EvaluatePosts
from utilities.email.EmailVariants.DailyReport import DailyReport
from utilities.logger.MyLogger import MyLogger
from config import config
from utilities.request.Request import Request
from json.decoder import JSONDecodeError
from utilities.filedriver.Local import Local

class Daily:

	def __init__(self, browser):
		self.browser = browser

	def evaluatePosts(self):
		Email(EvaluatePosts()).send()

	def dailyReport(self):
		self.browser.get("https://www.instagram.com/" + config.instagram_username + "/")
		followerCount = self.browser.find_element_by_css_selector("a[href*='followers'] span").text
		followingCount = self.browser.find_element_by_css_selector("a[href*='following'] span").text

		Request().post("/report/follower-count", {"followerCount": followerCount, "followingCount": followingCount})

		Email(DailyReport(followerCount, followingCount)).send()

	def reportErrors(self):
		MyLogger().send()
		MyLogger().empty()

	def cleanOutScrapedImages(self):
		local = Local()
		try:
			# fetch images that have been disapproved or that have been posted
		    filepaths = Request().get("/post/can-be-deleted").json()
		    for filepath in filepaths:
		     	# check if the images exist in scraped images and delete them
		    	local.deleteIfExists(filepath)
		   
		except JSONDecodeError:
		    print("no posts to delete")
		


