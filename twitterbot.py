import os
import random
import time

from markovbot.markovbot import MarkovBot

TWITTER_CONSUMER_KEY = 'vRVNJ06D2knfP5Sf3e50xkQJW'
TWITTER_CONSUMER_SECRET = 'cc6fEloGOKJiLftUD29YZkEKR0AVwlr0B8w0Xd76gYDoabduAw'
TWITTER_ACCESS_TOKEN = '878695267939344385-KGAzieOK8G4SAm7Pp4Ktladroz2biiG'
TWITTER_ACCESS_SECRET = 'n712umQqKOcKSrSJqpVw73ihbJrOnWg0YRtDC3FbKHByJ'

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
bot.twitter_tweeting_start(days=0, hours=1, minutes=3, keywords=None)

def wait():
    secsinhour = 60 * 60
    time.sleep(secsinhour)
    wait()

wait()
