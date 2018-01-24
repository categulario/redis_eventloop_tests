import redis

def loop():
    r = redis.StrictRedis()
    ps = r.pubsub()
    ps.subscribe('test_channel')

    while True:
        msg = ps.get_message(timeout=1.0)

        if msg:
            print(msg)

if __name__ == '__main__':
    loop()
