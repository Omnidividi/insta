from selenium.webdriver.common.action_chains import ActionChains
from utilities.request.Request import Request
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from follow.FollowExceptions import FollowExceptions
from time import sleep


class AutoFollow:

	def __init__ (self, browser):
		self.browser = browser

	def followFromUser(self, username, limit):
		self.browser.get("https://www.instagram.com/" + username + "/")
		sleep(2)
		followerButton = followerButton = self.browser.find_element_by_css_selector("a[href*='followers']")
		followerButton.click()
		sleep(2)
		followContainers = self.browser.find_elements_by_css_selector("li._6e4x5 div._npuc5")
		body = self.browser.find_element_by_tag_name("body")

		peopleFollowed = []
		followContainerIndex = 1

		while len(peopleFollowed) < limit:

			try:
			    currentFollowContainer = followContainers[followContainerIndex]
			    twoFollowContainersLater = followContainers[followContainerIndex + 2]
				## always move two fields on so that "currentFollowButton" is not under instagram bottom bar
			except IndexError:
				body.send_keys(Keys.END)
				newFollowContainers = self.browser.find_elements_by_css_selector("li._6e4x5 div._npuc5")
				indexOfLastClickedFollowContainer = newFollowContainers.index(lastClickedFollowContainer)
				followContainers = newFollowContainers
				followContainerIndex = indexOfLastClickedFollowContainer
				continue

			try:
				currentFollowButton = currentFollowContainer.find_element_by_css_selector("button._qv64e._gexxb._4tgw8._njrw0") 
				# self.highlight(currentFollowButton) ### for testing purposes
			except NoSuchElementException:
				## user is already being followed
				followContainerIndex += 1
				continue


			ActionChains(self.browser).move_to_element(twoFollowContainersLater)\
			.click(currentFollowButton)\
			.perform()
			sleep(1)

			buttonClass = currentFollowButton.get_attribute("class")
			followClass = "_qv64e _gexxb _4tgw8 _njrw0"
			if buttonClass == followClass:
				# this means that instagram has blocked me from following
				raise FollowExceptions.InstagramBlocksFollow()
				break

			usernameAnchor = currentFollowContainer.find_element_by_css_selector("div._eryrc div._2nunc a._2g7d5._o5iw8")
			usernameFollowed = usernameAnchor.get_attribute("title")
			peopleFollowed.append(usernameFollowed)
			followContainerIndex += 1

			lastClickedFollowContainer = currentFollowContainer

		self.recordNewFollowings(peopleFollowed)

	def recordNewFollowings(self, newFollowings):
		followingParameters = {"followed": newFollowings}
		request = Request().post("/followed/follow", json=followingParameters)

		reportParameters = {"followed" : len(newFollowings)}
		Request().post("/report/daily-report/increase", reportParameters)



	def highlight(self, element): ### for testing purposes
	    def apply_style(s):
	        self.browser.execute_script("arguments[0].setAttribute('style', arguments[1]);",
	                              element, s)
	    original_style = element.get_attribute('style')
	    apply_style("background: yellow; border: 2px solid red;")
	    sleep(1)
	    apply_style(original_style)
	