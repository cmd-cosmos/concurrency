### Locks and Queues
# synchronization primitives are important maily because of race conditions in concurrent systems.
import random
import asyncio
import time

async def coroutine(lock):
    print('Attempting to gain lock access')

    async with lock:
        print("locked")
        time.sleep(2)

    print("unclocked from the critical section")

async def main():
    lock = asyncio.Lock()
    task = asyncio.create_task(coroutine(lock))
    task2 = asyncio.create_task(coroutine(lock))
    await asyncio.wait([task, task2]) # completes both coroutines --> same coroutine twice.


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("coroutines over, closing loop")
loop.close()

### Queues: producer and consumer queues

async def producer(queue):
    while True:
        await asyncio.sleep(1)
        print("producing data")
        await queue.put(random.randint(1,5))

async def consumer(id, queue):
    print(queue)
    while True:
        print("consumer : {} attempting to get from queue".format(id))
        item = await queue.get()
        if item is None:
            break
        print("consumer: {} consumed article with id: {}".format(id, item))

async def main():
    queue = asyncio.Queue(maxsize=10)

    producer_task = asyncio.create_task(producer(queue=queue))
    consumer_task = [asyncio.create_task(consumer(1, queue=queue)),
                     asyncio.create_task(consumer(2, queue=queue))]

    await asyncio.sleep(5)

    for _ in consumer_task:
        await queue.put(None)

    await asyncio.gather(*consumer_task)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass
