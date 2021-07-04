from collect_tweets import collect_tweets
from generate_text import generate_sentence
from post_tweet import post_tweet


def main():
    collect_tweets('hirox246')

    sentences = generate_sentence(10, '/tmp/tweets.txt')

    [print(sentence) for sentence in sentences]

    post_tweet(sentences[0])


if __name__ == "__main__":
    main()
