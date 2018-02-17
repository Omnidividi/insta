from random import randrange
import time
import datetime
from datetime import timedelta
from config import config
import pickle

class DailyVars:

	def __init__(self):
		try:
			self.vars = self.load_obj("vars")
		except (OSError, IOError) as e:
			self.generateNewVars()
			self.vars = self.load_obj("vars")

		if self.vars["date"] != self.today():
			self.generateNewVars()
			self.vars = self.load_obj("vars")


	def today(self):
		return datetime.datetime.today().strftime('%Y-%m-%d')

	def save_obj(self, obj, name ):
	    with open("./" + name + '.pkl', 'wb') as f:
	        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

	def load_obj(self, name ):
	    with open("./" + name + '.pkl', 'rb') as f:
	        return pickle.load(f)

	def generateNewVars(self):
		dailyTimes = {
			"vars": {
				"follow": [],
				"unfollow": [],
				"post": [],
			},
			"date": self.today(),
		}

		for _ in range(config.follow_batches):
			dailyTimes["vars"]["follow"].append({"complete": 0, "time": self.random_date()})

		for _ in range(config.unfollow_batches):
			dailyTimes["vars"]["unfollow"].append({"complete": 0, "time": self.random_date()})

		for _ in range(config.posts_per_day):
			dailyTimes["vars"]["post"].append({"complete": 0, "time": self.random_date()})
		
		self.save_obj(dailyTimes, "vars")


	def random_date(self):
		todayYMD = datetime.datetime.today().strftime('%Y-%m-%d')
		start = todayYMD + " " + config.start_at_h + ":" + config.start_at_m
		end = todayYMD + " " + config.end_at_h + ":" + config.end_at_m
		start_timestamp = time.mktime(time.strptime(start, '%Y-%m-%d %H:%M'))
		end_timestamp = time.mktime(time.strptime(end, '%Y-%m-%d %H:%M'))
		randomTime = time.strftime('%Y-%m-%d %H:%M', time.localtime(randrange(start_timestamp,end_timestamp)))

		return randomTime

	def should(self, key):
		times = self.vars["vars"][key]
		nonCompletedTimes = [time['time'] for time in times if time['complete'] == 0]
		if len(nonCompletedTimes) == 0:
			return False
			
		earliestNonCompleted = min(nonCompletedTimes)
		nowStrToTime = time.time()
		nowString = datetime.datetime.fromtimestamp(nowStrToTime).strftime('%Y-%m-%d %H:%M')

		if earliestNonCompleted <= nowString:
			[var.update({"complete" : 1}) for var in self.vars["vars"][key] if var["time"] == earliestNonCompleted]
			self.save_obj(self.vars, "vars")
			return True
		else:
			return False
		# get earliest
		# see if earlier than now
			# if it is then return true and set complete to 1
		# else
			# return
		





