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

seedwords = [] #['computers', 'running', 'marathon', 'PHP', 'fuck', 'bagel', 'cat']

# text = bot.generate_text(size, seedwords)
# print("tweetbot says:")
# print(text)

# Tweet it
bot.twitter_login(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
bot.twitter_tweeting_start(days=0, hours=1, minutes=3, keywords=None)

def wait():
    secsinhour = 60 * 60
    time.sleep(secsinhour)
    wait()

wait()
