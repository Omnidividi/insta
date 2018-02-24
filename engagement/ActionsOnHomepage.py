from selenium import webdriver
from time import sleep
from engagement.auto_action import autoAction
from selenium.webdriver.common.action_chains import ActionChains

class actionsOnHomepage:

	def __init__ (self, browser):
		self.browser = browser
		self.actions = autoAction(browser)

	def like(self, limit):
		self.scroll(self.actions.like, limit)

	def comment(self, limit):
		self.scroll(self.actions.comment, limit)

	def scroll(self, actionToPerform, limit): ################################
		registeredPosts = []
		while len(self.usernamesOfPostsThatHaveBeenEngagedWith) < limit:
			newPosts = self.browser.find_elements_by_tag_name("article")
			posts = list(set(newPosts) - set(registeredPosts))
			registeredPosts.extend(posts)
			print("registered posts length")
			print(len(registeredPosts))
			if len(posts) != 0:
				for post in posts:
					try:
						print("index")
						print(registeredPosts.index(post))
						ActionChains(self.browser).move_to_element(post).perform()
						self.performActionOnDistinctPosts(actionToPerform, post)
						sleep(2)
					except:
						print("exception")
						continue
			else:
				# move to last currently showing post
				ActionChains(self.browser).move_to_element(newPosts[-1]).perform()
				sleep(2)

	usernamesOfPostsThatHaveBeenEngagedWith = []

	def performActionOnDistinctPosts(self, actionToPerform, post):
		if self.distinctNewsFeedPost(post):
			actionPerformed = actionToPerform(post)
			print(actionPerformed)
			if actionPerformed:
				usernameOfPost = self.userNameFromPost(post)
				self.usernamesOfPostsThatHaveBeenEngagedWith.append(usernameOfPost)
		else:
			print("post is not distinct")

	def distinctNewsFeedPost(self, post):
		thisPostName = self.userNameFromPost(post)
		return self.usernamesOfPostsThatHaveBeenEngagedWith.count(thisPostName) == 0

	def userNameFromPost(self, post): 
		nameAnchor = post.find_element_by_css_selector("a._2g7d5._iadoq")
		userName = nameAnchor.get_attribute("title")
		return userName