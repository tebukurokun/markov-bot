# coding:utf-8

import re
import tweepy

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


# Tweetの検索結果を標準出力
def printTweetBySearch(s: str):
    api = authTwitter()  # 認証

    tweets = tweepy.Cursor(api.search, q=s,
                           include_entities=True,
                           tweet_mode='extended',
                           lang='ja').items()  # # 省略されたリンクを全て取得 省略されたツイートを全て取得 日本のツイートのみ取得

    for tweet in tweets:
        if tweet.favorite_count + tweet.retweet_count >= 100:
            print('＝＝＝＝＝＝＝＝＝＝')
            print('twid : ', tweet.id)  # tweetのIDを出力。ユニークなもの
            print('user : ', tweet.user.screen_name)  # ユーザー名
            print('date : ', tweet.created_at)  # 呟いた日時
            print(tweet.full_text)  # ツイート内容
            print('favo : ', tweet.favorite_count)  # ツイートのいいね数
            print('retw : ', tweet.retweet_count)  # ツイートのリツイート数


# ユーザーのTweetを取得
def get_tweets_by_user(user_id: str):
    api = authTwitter()  # 認証

    tweets = tweepy.Cursor(api.user_timeline, id=user_id,
                           include_entities=True,
                           tweet_mode='extended',
                           lang='ja').items(200)  # # 省略されたリンクを全て取得 省略されたツイートを全て取得 日本のツイートのみ取得

    tweet_list = []

    for tweet in tweets:
        text = tweet.full_text
        text = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
        text = re.sub('@.+\s', "", text)
        text = re.sub('\n+', '\n', text)
        text = re.sub('RT ', '', text)

        tweet_list.append(text)

        print(text)

    return tweet_list


def main():
    print('collect tweet beginning…')
    tweets = get_tweets_by_user('hirox246')

    with open("hiroyuki.txt", "wt") as fout:
        for tweet in tweets:
            print(tweet, file=fout)

    print('collect tweet ending…')


if __name__ == "__main__":
    main()
