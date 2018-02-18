import os

class config:

	bot_account_id="__feel.fit__"
	base_website="http://london-pt.co.uk"

	# credentials
	username="feelfit.master@gmail.com"
	instagram_username="__feel.fit__"
	password="f33lF!t59" # don't use this password for other account in case they get hacked

	# timing
	start_at_h="08" # start program at hour MUST BE ZERO PADDED (eg. 09)
	start_at_m="00" # start program at minute MUST BE ZERO PADDED (eg. 09)
	end_at_h="19"	# End program at the hour MUST BE ZERO PADDED (eg. 09)
	end_at_m="00"	# End program at the min MUST BE ZERO PADDED (eg. 09)


	# limits
	like_per_day=200 # likes per day
	comments_per_day=200 # Max Comments per day
	follow_per_day=100 # people to follow per day
	number_of_people_to_follow_per_user=20 # the number of people to follow per individual user I am scraping followers from
	follow_time=5*60*60 # Seconds to wait before unfollowing
	unfollow_per_day=100 # Max Users to unfollow per day
	posts_per_day=2 # how many photos to post per day
	post_backlog=40 # how many unposted, saved photos that are scheduled to be posted there should be on average
	times_of_posts=[] # array of possible times to post pictures
	## NOTE:
	# follow_per_day should equal unfollow_per_day (unless you want to have more followers than unfollowers)
	# also your average follow count will be your follow_time (IN DAYS) multiplied by the number of people you follow per day
	# example: if you unfollow people after 4 days and follow 200 people a day, your average follower count will hover around 800

	# follow specific
	follow_batches=4 # the amount of batches the total daily follower count should be broken up into
	break_between_follow_batches=[1*60*60,3*60*60] # the [min,max] time between follow batch execution
	unfollow_batches=4 # the amount of batches the total daily follower count should be broken up into
	break_between_unfollow_batches=[1*60*60,3*60*60] # the [min,max] time between follow batch execution

	# accounts
	account_to_scrape_followers_from=["bikini", "boutinelababes", "fitnessgirlsmotivation", "fit", "fitnesscave", "bikini_feed", "sexy.tang", "bikiniandother", "gymspire", "motivabikini", "fitnessbeautifuls", "fitness_0ne", "fitness_junkie", "amazingfitgirls", "livelifefit_na", "fit.summer_", "only.perfect.abs", "bikiniholist", "body_fitness_fashion", "bikini.4u", "bikinidolls", "fit.determination", "fitness.direction", "fit.instagr", "fitness.wonderful", "fit.omega"] # usernames of accounts to follow people from
	accounts_to_scrape_posts_from=["racheljdillon", "laurensimpson", "karinaelle", "caroline_omahony", "amandabisk", "toneitup", "hannahbronfman", "gypsetgoddess", "kayla_itsines", "kaisafit", "emilyskyefit", "basebodybabes", "jenselter", "fitnessontoast", "massy.arias", "annavictoria", "tracyandersonmethod", "yoga_girl", "natalieuhling", "blogilates", "msjeanettejenkins", "AmandaBisk", "EmilySkyeFit", "FollowtheLita", "GetBodiedByJ", "LyzabethLopez", "michelle_lewin", "NatalieJillFit", "Kayla_Itsines", "AnnaVictoria", "AnaCheri", "BrittanyPerillee", "katyaelisehenry", "paigehathaway", "followthelita", "natalieuhling", "anadeliafitness", "bellafalconi", "christmasabbott", "annavictoria", "blogilates", "aurora_LZ_Fit", "realheidipowell", "lyzabethlopez", "karenakatrina", "nataliejillfit", "msjeanettejenkins", "massy.arias", "jenwiderstrom", "kayla_itsines", "amandaeliselee", "hunnybunsfit", "camillelbaz", "emilyskyefit", "shadesofjoy.co", "tanaashleee", "carmelrodriguezfit", "emilyschromm", "ashleymfreeman", "amandabisk", "hannahbronfman", "kayla_itsines", "msjeanettejenkins", "natalieuhling", "annavictoria", "massy.arias", "amandabisk", "ivfitness", "michelle_lewin", "lyzabethlopez", "censkiii", "tmiller_fit", "clind", "fitandfiesty", "genesislopezfitness", "sommerray", "emily.tala", "majenyrose", "bryanaholly", "_cassiebrown_", "jadegrobler", "keilah.k", "amberrdaviss", "galina.dub", "viki_odintcova", "kaylasheag", "jacquelynnoelle", "galina_dub", "popstantot", "mathildtantot", "iblowurmind", "isabellemathersx", "elisha__h", "anllela_sagra", "anllelasagra_", "iamyanetgarcia", "sandraprikker", "galina_dub", "juliagilas", "philineroepstorff", "iblowurmind", "popstantot", "mathildtantot", "sierraaaskyee", "puppiesofinstagram", "puppytoday", "instapuppers", "bikini", "boutinelababes", "fitnessgirlsmotivation", "fit", "fitnesscave", "bikini_feed", "sexy.tang", "bikiniandother", "gymspire", "motivabikini", "fitnessbeautifuls", "fitness_0ne", "fitness_junkie", "amazingfitgirls", "livelifefit_na", "fit.summer_", "only.perfect.abs", "bikiniholist", "body_fitness_fashion", "bikini.4u", "bikinidolls", "fit.determination", "fitness.direction", "fit.instagr", "fitness.wonderful", "fit.omega", "detoxpage"] # usernames of accounts to scrape posts from

	# emails
	master_email="feelfit.master@gmail.com" # email address to send emails to in case of: dialy reports, direct messages,
	this_account_email="feelfit.master@gmail.com" # email address of this account. The sender address for all emails in this bot
	this_account_email_password="f33lF!t59" # email password of this account

	# hashtags
	hashtag_blacklist=["ad", "advert", "sponsored", "advertisement", "giveaway"] # hashtags of pictures that should not be reposted
	post_hashtag=["fitness", "bikini", "body", "goals"] # hashtags to add to posts

	# comments
	captions = ["😍","😱","👑"]

	base_path=os.path.dirname(os.path.abspath(__file__))
	# filedriver options
	filedriver="local"
	local_path=base_path + "/scrape/ScrapedImages/"
	# logging options
	log_path=base_path + "/utilities/logger/errors.log"

	# proxy
	#proxy	str	Access instagram through a proxy. (host:port or user:password@host:port)
	proxy=""
	use_proxy=False

	# headless
	headless=True # setting headless to true will make the browser window not appear even if the bot is runnings



