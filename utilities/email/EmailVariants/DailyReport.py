from config import config
from utilities.request.Request import Request
import datetime

class DailyReport:

	def __init__(self, totalFollowerCount, totalFollowingCount):
		self.totalFollowerCount = totalFollowerCount
		self.totalFollowingCount = totalFollowingCount
		self.generateMessage()
		self.generateSubject()

	recipient = config.master_email
	subject = ""
	message = ""
	attachmentAvailable = False

	def generateMessage(self):
		dailyStats = Request().get("/report/daily-report/fetch").json()

		likedToday = "{} posts were liked today.".format(dailyStats["liked"])
		commentedToday = "{} posts were commented on today.".format(dailyStats["commented"])
		followedToday = "{} users have been followed today.".format(dailyStats["followed"])
		unfollowedToday = "{} users have been unfollowed today.".format(dailyStats["unfollowed"])
		postedToday = "{} pictures were posted today".format(dailyStats["posted"])
		totalFollowers = "Total follower count is: {}".format(self.totalFollowerCount)
		totalFollowing = "Total following count is: {}".format(self.totalFollowingCount)

		messageText = "{}\n{}\n{}\n{}\n{}\n{}\n{}\n"
		finalMessage = messageText.format(likedToday, commentedToday, followedToday, unfollowedToday, postedToday, totalFollowers, totalFollowing)
		self.message = finalMessage

	def generateSubject(self):
		self.subject = "Daily Report For {}, for the {}".format(config.bot_account_id, datetime.date.today())