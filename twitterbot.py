import os
import random
import time

from markovbot.markovbot import MarkovBot

TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_SECRET = ''

# Initialize bot
bot = MarkovBot()

# Get the source
dirname = os.path.dirname(os.path.abspath(__file__))
source = os.path.join(dirname, 'source.txt')

# Read the source
bot.read(source)

# Determine the size of the tweet
size = random.randint(5, 25)

# Tweet it
bot.twitter_login(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
bot.twitter_tweeting_start(days=0, hours=0, minutes=1, keywords=None)

def wait():
    secsinweek = 7 * 24 * 60 * 60
    time.sleep(secsinweek)
    wait()

wait()
