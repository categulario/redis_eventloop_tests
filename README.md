# Comparing two redis listener models

An experiment on how an event listener loop in python+redis should be.

The two models to compare are the folowing:

## Sleep loop

As sugested in the [redis-py](https://github.com/andymccurdy/redis-py) site, a loop that requests a message from the socket and then sleeps:

```python
def loop():
    while True:
        ps.get_message()
        time.sleep(0.001) # run 1000 times a second
```

In this model one adjusts the sleep time to match this serice's expected throughput. The smaller the time, the better response. But also more iterations per second mean more CPU usage.

## Timeout loop

This model requests a message from the socket with a specified timeout:

```python
def loop():
    while True:
        ps.get_message(timeout=1.0)
```

With no load, this models consumes 1 cycle per second, which is like being kind to the CPU. With high load the loop's response speed limit depends only on the CPU itself since there is no pause between one `get_message` call and the next one if both return a message.

## Results

The *sleep* model consumes way more CPU than the *timeout* model.

## Try yourself

* `virtualenv .env`
* `source .env/bin/activate`
* `pip install -r requirements.txt`
* `./run.sh <one of the scripts>`

Now send some messages from redis-cli:

* `redis-cli`
* `publish test_channel a_message`
