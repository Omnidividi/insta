import logging
from utilities.email.EmailDriver import Email
from utilities.email.EmailVariants.ErrorLogEmail import ErrorLogEmail

class MyLogger:

	def __init__(self):
		logging.basicConfig(filename='errors.log',level=logging.DEBUG)
		stream_handler = logging.StreamHandler()
		formatter = logging.Formatter("%(levelname)s : %(pathname)s:%(lineno)s - %(msg)s --- %(asctime)s")
		stream_handler.setFormatter(formatter)

		logger = logging.getLogger('foo')
		logger.addHandler(stream_handler)
		logger.setLevel(logging.DEBUG)

		

	def log(self, error):
		logging.error("\n --------------------------------- \n", exc_info=True)
		logging.error(error, exc_info=True)
		logging.error("\n --------------------------------- \n", exc_info=True)

	def empty(self):
		with open("errors.log", "w") as file:
			file.truncate()

	def send(self):
		Email(ErrorLogEmail()).send()
