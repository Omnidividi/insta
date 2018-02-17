from config import config
from time import sleep
from scrape.Post import Post
from scrape.ScrapeExceptions import ScrapeExceptions
import random

class UserScraper:

	def __init__(self, browser):
		self.browser = browser
		self.possibleUsersToScrapeFrom = config.accounts_to_scrape_posts_from
		self.numberOfPostToScrape = config.posts_per_day
		self.usersScrapingHasBeenAttemptedOn = []

	def run(self):
		# 1: Find a random user from user list
		randomUsername = self.fetchRandomUser()


		try:
			self.fetchRandomPostObject(randomUsername).scrape()
		except ScrapeExceptions.NotEnoughPostsFoundForThisSearchCriteria as e:
			# if not enough posts were found then just skip this user
			return

	def fetchRandomUser(self):
		# find users that were not previously selected and shuffle them
		notPreviouslySelectedUsernames = list(set(self.possibleUsersToScrapeFrom) - set(self.usersScrapingHasBeenAttemptedOn))
		random.shuffle(notPreviouslySelectedUsernames)
		# check if there are any users left
		if len(notPreviouslySelectedUsernames) == 0:
			raise ScrapeExceptions.NotEnoughPostsFound()
		# take first user
		randomUsername = notPreviouslySelectedUsernames[0]
		# record and return random user
		self.usersScrapingHasBeenAttemptedOn.append(randomUsername)
		return randomUsername



	def fetchRandomPostObject(self, username):
		postFound = False
		postsAttempted = 0
		randomPostTried = []


		while not postFound:

			# 1: find posts
			self.browser.get("https://www.instagram.com/" + username + "/")
			sleep(2)
			try:
				error = self.browser.find_element_by_css_selector("error-container")
				MyLogger().log("!!!!!!!!!!!!!!! " + username + " does not exist !!!!!!!!!!")
				raise ScrapeExceptions.NotEnoughPostsFoundForThisSearchCriteria()
			except:
				break
				# continue as per usual
			posts = self.browser.find_elements_by_css_selector("div._mck9w._gvoze._tn0ps")
			postNumber = len(posts)
			randomPostNumber = random.randint(1, postNumber)

			# 2: select random post number - must be within range, random and not previously selected
			while randomPostNumber in randomPostTried:
				randomPostNumber = random.randint(1, postNumber)

			# 3: select post
			randomPost = posts[randomPostNumber - 1]
			randomPostTried.append(randomPostNumber)
			randomPostUrl = randomPost.find_element_by_css_selector("a").get_attribute("href")

			# 4: create post object
			postObject = Post(randomPostUrl, self.browser)

			# 5: check if post is eligible
			if postObject.eligibleForScraping():
				postFound = True
				return postObject

			# 6: if post is not eligibile, record that another post has been checked
			# if all posts are checked and still no post is found then return false
			postsAttempted += 1
			if postsAttempted == postNumber:
				raise ScrapeExceptions.NotEnoughPostsFoundForThisSearchCriteria()





