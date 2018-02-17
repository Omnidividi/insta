import urllib
from scrape.ScrapeExceptions import ScrapeExceptions
import os
from config import config
from pathlib import Path
from utilities.logger.MyLogger import MyLogger

class Local:

	#### move this to saveLocation
	def download(self, postInstance):
		try:
			imagePath = config.local_path + postInstance.instaId + ".jpg"
			urllib.request.urlretrieve(postInstance.imageUrl, imagePath)
			return postInstance.instaId
		except Exception as e:
			MyLogger().log(e)
			raise ScrapeExceptions.FileSaveError()
		
	def get(self, filePath):
		return config.local_path + filePath + ".jpg"

	def deleteIfExists(self, filePath):
		fullFilePath = config.local_path + filePath + ".jpg"
		if os.path.exists(fullFilePath):
			os.remove(fullFilePath)
    