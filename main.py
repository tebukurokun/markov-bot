from collect_tweets import collect_tweets
from generate_text import generate_sentence
from post_tweet import post_tweet


def main():
    print('*** start ***')

    collect_tweets('hirox246')

    sentences = generate_sentence(10, '/tmp/tweets.txt')

    [print(sentence) for sentence in sentences]

    post_tweet(sentences[0])

    print('*** end ***')


if __name__ == "__main__":
    main()
