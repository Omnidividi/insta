from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

class autoAction:

	def __init__(self, browser):
		self.browser = browser


	def like(self, post):
		# like image
		if not self.postHasBeenLiked(post):
			return self.clickHeart(post)
		else:
			return False

	def dislike(self, post):
		# like image
		if self.postHasBeenLiked(post):
			return self.clickHeart(post)
		else:
			return False

	def toggleLike(self, post):
		return self.clickHeart(post)

	def clickHeart(self, post):
		try:
			likeButton = post.find_element_by_css_selector("a._eszkz._l9yih")
			likeButton.click()
			# image has already been liked
		except NoSuchElementException: 
			return False

		return True

	def postHasBeenLiked(self, post):
		try:
			fullHeartLikedButton = post.find_element_by_css_selector("span._8scx2.coreSpriteHeartFull")
			return True
		except NoSuchElementException:
			try:
				emptyHeartLikedButton = post.find_element_by_css_selector("span._8scx2.coreSpriteHeartOpen")
				return False
			except NoSuchElementException:
				print("error, no liked or dislike button found")

		return False

	def comment(self, post, comment="Nice Post!"):
		# check if I have already commented
		if self.postHasCommentByMe(post):
			return False
		else:
			try:
				commentButton = post.find_element_by_css_selector("a._p6oxf._6p9ga")
				ActionChains(self.browser).move_to_element(commentButton).click(commentButton).perform()
				# wait till input shows up
				sleep(3)
				commentInput = post.find_element_by_css_selector("textarea._bilrf")
				ActionChains(self.browser).move_to_element(commentInput).send_keys(comment).perform()
				sleep(2)
				# submitButton = post.find_element_by_css_selector("button._55p7a")
				# submitButton.click()
				return True
			except:
				print("there has been in error whilst commenting")

	def postHasCommentByMe(self, post):
		# check if I have already commented
		# self.loadAllComments(post) --- I don't think I need to load all comments since, if i have commented on the picture,
		# instagram would make my comment show up right away
		allCommentUsers = post.find_elements_by_css_selector("li._ezgzd a._2g7d5._95hvo")
		commentsWithMyUsername = filter(self.isCommentByMe, allCommentUsers)
		return commentsWithMyUsername == 0

	def loadAllComments(self, post):
		for _ in range(3):
			try:
				loadMoreCommentsButton = post.find_element_by_css_selector("a._m3m1c._1s3cd")
				ActionChains(self.browser).move_to_element(loadMoreCommentsButton).click(loadMoreCommentsButton).perform()
			except NoSuchElementException:
				break
			except:
				print("not clickable")

	def isCommentByMe(self, comment):
		myUserName = "officialtrainex" # should be global constant
		commentUserName = comment.get_attribute("title")
		return myUserName == commentUserName