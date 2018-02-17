from selenium import webdriver
from time import sleep
from engagement.auto_action import autoAction
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random

class actionsOnUser:

	def __init__ (self, browser, username):
		self.browser = browser
		self.actions = autoAction(browser)
		self.username = username
		self.navigateToUser()

	def navigateToUser(self):
		self.browser.get("https://www.instagram.com/" + self.username + "/")

	def like(self, limit):
		self.performActionOnRecentPosts(self.actions.like, limit)

	def comment(self, limit):
		self.performActionOnRecentPosts(self.actions.comment, limit)

	def performActionOnRecentPosts(self, actionToPerform, limit):
		sleep(2)
		postsThatHaveBeenEngagedWith = 0
		mostRecentPosts = self.mostRecentPosts(limit)
		numberOfPosts = len(mostRecentPosts)
		limit = limit if limit < numberOfPosts else numberOfPosts # so that limit is not higher than the actual number of posts
		for i in range(numberOfPosts):
			if postsThatHaveBeenEngagedWith == limit:
				break
			
			mostRecentPosts = self.mostRecentPosts(limit)
			currentPost = mostRecentPosts[i]

			# visit post url
			currentPost.click()
			sleep(2)
			fullSizedPost = self.browser.find_element_by_css_selector("article._7hhq6._622au._fsupd._8n9ix") 
			# perform action
			print("about to perform action")
			actionPerformed = actionToPerform(fullSizedPost)
			sleep(3)
			if actionPerformed:
				postsThatHaveBeenEngagedWith += 1
				
			# go back to user's page
			self.navigateToUser()
			sleep(2)
		
		print("number of posts intended to engage with: " + str(limit))
		print("number of posts actually engaged with: " + str(postsThatHaveBeenEngagedWith))

	def mostRecentPosts(self, limit):
		mostRecentPosts = []
		allPosts = self.browser.find_elements_by_css_selector("div._mck9w._gvoze._tn0ps")
		numberOfPosts = len(allPosts)
		if numberOfPosts > 20:
			mostRecentPosts = allPosts[:20]
		return mostRecentPosts
		# this method returns either all the most recent posts, or (if there are more than 20 recent posts) only the last 20
