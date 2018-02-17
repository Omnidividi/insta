from post.Caption import Caption
from time import sleep
from utilities.request.Request import Request
from selenium.webdriver.common.action_chains import ActionChains
import os
from utilities.filedriver.Local import Local
from json.decoder import JSONDecodeError
from config import config

class Poster:

	def __init__(self, browser):
		self.browser = browser

	def run(self):
		# check if there is an outstanding post to be posted in db
		if self.uploadLimitNotReached():
			try:
				self.outstandingPost = self.outstandingPost()
				caption = Caption(self.outstandingPost).generate()
				imagePath = self.outstandingPost["file_path"]
				imagePath = Local().get(imagePath)
				self.uploadPost(imagePath, caption)
			except JSONDecodeError:
				print("no more outstanding posts")

	def uploadLimitNotReached(self):
		postsPerDay = config.posts_per_day
		alreadyPostedToday = Request().get("/report/daily-report/fetch").json()["followed"]
		return alreadyPostedToday < postsPerDay

	def outstandingPost(self):
		request = Request().get("/post/fetch")
		sleep(10)
		return request.json()

	def uploadPost(self, imagePath, caption):
		self.browser.get("https://instagram.com")

		addImageButton = self.browser.find_element_by_css_selector("div._k0d2z._ttgfw._mdf8w")
		addImageButton.click()

		bottomBar = self.browser.find_element_by_css_selector("nav._68u16._evlcw")
		imageInput = bottomBar.find_element_by_css_selector("input._l8al6")
		# filepath = os.getcwd()+imagePath

		imageInput.send_keys(imagePath)

		sleep(5)

		# fullsizeButton = self.browser.find_element_by_css_selector("button._j7nl9")
		# fullsizeButton.click()
		nextButton = self.browser.find_element_by_css_selector("button._9glb8")
		nextButton.click()

		sleep(5)

		captionInput = self.browser.find_element_by_css_selector("textarea._qlp0q")
		shareButton = self.browser.find_element_by_css_selector("button._9glb8")

		sleep(2)
		ActionChains(self.browser).move_to_element(captionInput)\
			.click()\
			.send_keys(caption)\
			.click(shareButton)\
			.perform()

		Request().get("/post/posted/" + self.outstandingPost["insta_id"]);













	