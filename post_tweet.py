from sudachipy import tokenizer
from sudachipy import dictionary
import markovify
import re
from glob import iglob
import tweepy

import collect_tweets
import credential

CK = credential.CONSUMER_KEY
CS = credential.CONSUMER_SECRET
AT = credential.ACCESS_TOKEN_KEY
AS = credential.ACCESS_TOKEN_SECRET


# TwitterAPI認証用関数
def authTwitter():
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, AS)
    api = tweepy.API(auth, wait_on_rate_limit=True)  # API利用制限にかかった場合、解除まで待機する
    return api


def post_tweet(text: str):
    print('post_tweet beginning')

    api = authTwitter()  # 認証

    result = api.update_status(status=text)
    print(result)

    print('post_tweet ending')
