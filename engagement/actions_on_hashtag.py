from selenium import webdriver
from time import sleep

class actionsOnHashtag:

	def __init__(self, browser):
		self.browser = browser

	def forHashtag(self, hashtag)
		self.browser.get("https://www.instagram.com/explore/tags/fashion/" + hashtag)
		return self

	def follow(self, limit):

	def like(self, limit):