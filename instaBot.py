from selenium import webdriver
from time import sleep
from scrape.Scraper import Scraper
from scrape.Handlers.UserScraper import UserScraper
from login.AutoLogin import AutoLogin
from post.Poster import Poster
from follow.FollowManager import FollowManager
from daily.Daily import Daily
from config import config
from daily.DailyVars import DailyVars
from utilities.logger.MyLogger import MyLogger

class instaBot:

	def __init__(self):
		self.dailyVars = DailyVars()

		chrome_options = webdriver.ChromeOptions()
		mobile_emulation = { "deviceName": "iPhone 7" }
		chrome_options = webdriver.ChromeOptions()
		chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
		# chrome_options.add_argument("--incognito")
		if config.headless:
			chrome_options.add_argument('--headless')
			chrome_options.add_argument('--disable-gpu')  # Last I checked this was necessary.


		if config.use_proxy:
			myProxy = config.proxy

			proxy = Proxy({
				'proxyType': ProxyType.MANUAL,
				'httpProxy': myProxy,
				'ftpProxy': myProxy,
				'sslProxy': myProxy,
			})
			self.browser = webdriver.Chrome(chrome_options=chrome_options, proxy=proxy)
		else:
			self.browser = webdriver.Chrome(chrome_options=chrome_options)

		AutoLogin(self.browser).login()




	def run(self):

		# Scrape posts every time bot is fired
		scraper = Scraper(UserScraper(self.browser))
		scraper.run()

		if self.dailyVars.should("follow"):
			followManager.follow()

		if self.dailyVars.should("unfollow"):
			followManager.unfollow()

		if self.dailyVars.should("post"):
			poster = Poster(self.browser)
			poster.run()

		sleep(5)
		self.browser.close()
		return


		# except:
		# 	print("critical error, no user with good posts could be found")
		# do login
		# do likes
		# do follows
		# do unfollows
		# do posts
		# do comments

	def dailyWrapUp(self):
		dailyHandler = Daily(self.browser)
		# # send email to self with information about scraped posts, post backlog and post evaluation
		dailyHandler.evaluatePosts()
		# # send email to self about daily statistics and report to database the follower and following count
		dailyHandler.dailyReport()
		# # send email to self about errors that occured today
		dailyHandler.reportErrors()
		# delete all images that have been posted or disapproved to save space
		dailyHandler.cleanOutScrapedImages()

		sleep(5)
		self.browser.close()
		return







# to do

	# a function where it finds special posts for special days
		# eg. cheat day sunday - account finds cheat meal picture on saturday to post for sunday
	# video repost function
	# wait wait wait - instead of saving picture, why dont I just use the web_url to repost???????????
	# check likes on posts to repost to find the most popular
	# before saving a post, check if database has already saved it
	# manual submission of a post - the post is added to the database and to the scraped images
	# maybe also make mechanism to delete all the hastags off old posts - with fewer hashtags they look more legit
	# write script to handle if a bot gets to a page and it says the user is not available like: https://www.instagram.com/aurora_LZ_Fit/
	# go through and delete all the sleeps
	# MyLogger all errors
	# Upload and update from github so that all the projects are always consistant
	# do it so that the browser only opens and logs in if a task is really to be performed - otherwise if instagram is logged
	# into consistantly every hour, at the same time, instagram will get suspicious
	# make MyLogger log to a different file than the automatic error logger - errors.log is very hard to read
	# make it so that scrapper recognises whether a post is eligible for scraping (except for the hashtag criteria) before clicking on it





