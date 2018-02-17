from selenium import webdriver
from time import sleep
from config import config
from selenium.common.exceptions import NoSuchElementException
from follow.FollowExceptions import FollowExceptions
from utilities.request.Request import Request

class AutoUnfollow:

	def __init__ (self, browser):
		self.browser = browser

	def unfollowFromSelf(self, limit):
		self.browser.get("https://www.instagram.com/" + config.instagram_username + "/")

		sleep(2)
		followerButton = browser.find_element_by_css_selector("a[href*='followers']")
		followerButton.click()
		sleep(2)

		unfollowButtons = browser.find_elements_by_css_selector("button._qv64e._t78yp._4tgw8._njrw0")
		numberOfUnfollowButtons = len(unfollowButtons)

		maxLimit = numberOfUnfollowButtons if numberOfUnfollowButtons < limit else limit

		for x in range(1,maxLimit):
			unfollowButton = unfollowButtons[x]
			unfollowButton.click()


	def usersToUnfollow(self, users):
		usersUnfollowed = []
		usersAlreadyUnfollowed = []

		for user in users:
			username = user["username"]
			try:
				self.unfollow(username)
				usersUnfollowed.append(username)
			except FollowExceptions.UserAlreadyUnfollowed:
				# create two separate lists for unfollowed and already unfollowed because we don't want
				# the already unfollowed to be registered as newly unfollowed on the daily report
				usersAlreadyUnfollowed.append(username)

		unfollowingParameters = {"unfollowed": usersUnfollowed}
		Request().post("/followed/unfollow", json=unfollowingParameters)

		reportParameters = {"unfollowed" : len(usersUnfollowed)}
		Request().post("/report/daily-report/increase", reportParameters)

		alreadyUnfollowedParameters = {"unfollowed": usersAlreadyUnfollowed}
		Request().post("/followed/unfollow", json=alreadyUnfollowedParameters)

		


	def unfollow(self, username):
		self.browser.get("https://www.instagram.com/" + username + "/")
		sleep(2)
		try:
			unfollowButton = self.browser.find_element_by_css_selector("span._lyv4q._ov9ai").find_element_by_css_selector("button._qv64e._t78yp._r9b8f._njrw0")
			unfollowButton.click()
			sleep(2)
			# note in database that this user has been unfollowed
		except NoSuchElementException:
			# check whether this user has already been unfollowed (can see the "follow" button)
			raise FollowExceptions.UserAlreadyUnfollowed()





