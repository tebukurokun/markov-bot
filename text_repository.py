import redis

import redis_config

REDIS_HOST = redis_config.REDIS_HOST
REDIS_PORT = redis_config.REDIS_PORT
REDIS_PASSWORD = redis_config.REDIS_PASSWORD


class TextRepository:

    def __init__(self):
        try:
            # self.redis = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, password=REDIS_PASSWORD)
            self.redis = redis.from_url(redis_config.REDIS_URL)

            print('connected')

        except Exception as e:
            print(e)

    def update_text(self, key: str, text: str):
        """
        key に textを登録.
        :param key: str
        :param text: str
        :return: Any
        """
        print('update text start')

        result = self.redis.set(key, text)

        print('update text end')

        return result

    def get_text(self, key: str) -> str:
        print('get text start')

        res = str(self.redis.get(key).decode('utf-8'))

        print('get text end')

        return res

    def __del__(self):
        try:
            self.redis.close()

            print("disconnected")
        except Exception as e:
            print(e)
