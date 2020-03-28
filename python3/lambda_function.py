import json,os
import functions as tw
from twython import Twython, TwythonError

def lambda_handler(event, context):
    # TODO implement
    
    CONSUMER_KEY = os.environ['CONSUMER_KEY']
    CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    ACCESS_SECRET = os.environ['ACCESS_SECRET']
    MESSAGE=os.environ['MESSAGE']
    delta=tw.diff_time()
    msg=tw.pretty_time_delta(delta.total_seconds())
    tweet=tw.pretty_message(msg,MESSAGE)
    print('Tweet: ',tweet)
    try:
        twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
        print(twitter)
    except TwythonError as e:
        print(e)

    try:
        twitter.update_status(status=tweet)
    except TwythonError as e:
        print(e)

    #return 