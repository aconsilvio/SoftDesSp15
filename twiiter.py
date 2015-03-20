"""twitter stuff"""

import pattern
import time

from pattern.web import Twitter, plaintext
from pattern.en import parse
engine = Twitter(license=None, throttle=0.5, language=None)

twitter = Twitter(language='en')
def get_tweets(your_string, run_number):
	s = Twitter().stream(your_string)
	for i in range(run_number):
		time.sleep(1)
		s.update(bytes=1024)
		print s[-1].text if s else ''

def twitter_trends(rank):
	trend_list = Twitter().trends(cached=False)
	return trend_list[rank-1]

def get_tweets2(rank):
	your_string = twitter_trends(rank)
	i = None
	for tweet in twitter.search(your_string):
		tweet = plaintext(tweet.text)
	return tweet
#tweets = parse(tweets)

def list_of_tweets(rank):
	your_string = twitter_trends(rank)
	list_tweet = []
	for i in range(10):
		curr_tweet = get_tweets2(rank)
		if curr_tweet not in list_tweet:
			list_tweet.append(curr_tweet)
	print list_tweet


#print tweets

#list_of_tweets(4,10)
print list_of_tweets(3)