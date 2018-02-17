class FollowExceptions:

	class NoMoreAccountsToStealFollowersFrom(Exception):
	# When you have exhausted all possible instagram accounts on the steal followers from list
		pass

	class UserAlreadyUnfollowed(Exception):
	# When you try to unfollow user but he is already unfollowed
		pass

		