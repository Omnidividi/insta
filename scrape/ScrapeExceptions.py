class ScrapeExceptions:

	class NotEnoughPostsFound(Exception):
	# When overall not enough posts are found to scrape across all users and hashtags
		pass

	class NotEnoughPostsFoundForThisSearchCriteria(Exception):
	# When not enough posts are found for a specific user or specific hashtag
		pass
		
	class DatabaseError(Exception):
	# When the file information could not be saved to the database
		pass
		
	class FileSaveError(Exception):
	# When the file could not be saved to the disk
		pass
		
		