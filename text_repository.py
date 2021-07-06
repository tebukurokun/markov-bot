import redis

import redis_config

REDIS_HOST = redis_config.REDIS_HOST
REDIS_PORT = redis_config.REDIS_PORT
REDIS_PASSWORD = redis_config.REDIS_PASSWORD


class TextRepository:

    def __init__(self):
        try:
            self.redis = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0, password=REDIS_PASSWORD)
        except Exception as e:
            print(e)

    def update_text(self, key: str, text: str):
        """
        key に textを登録.
        :param key: str
        :param text: str
        :return: Any
        """
        result = self.redis.set(key, text)

        return result

    def get_text(self, key: str) -> str:
        res = str(self.redis.get(key).decode('utf-8'))

        return res

    def __del__(self):
        try:
            self.redis.close()
        except Exception as e:
            print(e)


if __name__ == "__main__":
    redis_manager = TextRepository()

    redis_manager.update_text("hiroyuki", "bbbbbb")

    t = redis_manager.get_text('hirox246')

    print(t)
