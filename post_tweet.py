from sudachipy import tokenizer
from sudachipy import dictionary
import markovify
import re
from glob import iglob
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


def load_file(file):
    _text = ''

    for path in iglob(file):
        with open(path, 'r', encoding='utf-8') as f:
            _text += f.read().strip()

    return _text


def split_input_files(text: str):
    _tokenizer_obj = dictionary.Dictionary().create()
    _mode = tokenizer.Tokenizer.SplitMode.C

    _splitted_text = ''

    _words = [m.surface() for m in _tokenizer_obj.tokenize(text, _mode)]

    for _word in _words:
        _word = re.sub(r'[（）「」『』｛｝【】＠”’！？｜～・]', '', _word)  # 全角のカッコ、各種記号は削除
        _word = re.sub(r'[()\[\]{}@\'\"!?|~-]', '', _word)  # 半角のカッコ、各種記号は削除
        _word = re.sub(r'\u3000', '', _word)  # 全角カッコは削除
        _word = re.sub(r' ', '', _word)  # 半角スペースは削除
        _word = re.sub(r'\n', '', _word)  # もともと存在する改行コードは削除

        _word = re.sub(r'。', '。\n', _word)  # 句点は改行コードを追加
        _word += ' '

        _splitted_text += _word

    return _splitted_text


def generate_sentence(exec_times: int, *files) -> list[str]:
    input_text = ''

    for file in files:
        input_text += load_file(file)

    splitted_text = split_input_files(input_text)

    text_model = markovify.NewlineText(splitted_text, state_size=2)  # markovify.Text()ではない

    markov_sentences = [text_model.make_short_sentence(140, min_chars=100, tries=100).replace(" ", "") for i in
                        range(exec_times)]

    return markov_sentences


def post_tweet(text: str):
    api = authTwitter()  # 認証

    result = api.update_status(status=text)
    print(result)


if __name__ == '__main__':
    sentences = generate_sentence(10, '/tmp/hiroyuki.txt')

    [print(sentence) for sentence in sentences]

    post_tweet(sentences[0])
