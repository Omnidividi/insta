from time import sleep
from config import config

class AutoLogin:

	def __init__(self, browser):
		self.browser = browser

	def login(self):
		self.navigateToLoginPage()
		self.fillInForm()

	def navigateToLoginPage(self):
		self.browser.get("https://www.instagram.com/accounts/login/")

	def fillInForm(self):
		username = config.username
		password = config.password

		usernameInput = self.browser.find_element_by_name("username")
		passwordInput = self.browser.find_element_by_name("password")

		usernameInput.send_keys(username)
		passwordInput.send_keys(password)

		loginButton = self.browser.find_element_by_xpath('//form/span/button[text()="Log in"]')
		loginButton.click()

		sleep(4)



