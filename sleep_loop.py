import redis
from time import sleep

def loop():
    r = redis.StrictRedis()
    ps = r.pubsub()
    ps.subscribe('test_channel')

    while True:
        msg = ps.get_message()

        if msg:
            print(msg)

        sleep(0.001) # run tousand times a second

if __name__ == '__main__':
    loop()
