import config
from generate_text import generate_sentence
from post_tweet import post_tweet

TWITTER_ID = config.TWITTER_ID


def main():
    print('*** start ***')

    sentences = generate_sentence(10, TWITTER_ID)

    [print(sentence) for sentence in sentences]

    post_tweet(sentences[0])

    print('*** end ***')


if __name__ == "__main__":
    main()
