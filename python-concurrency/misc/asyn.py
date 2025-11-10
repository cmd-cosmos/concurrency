#pylint: skip-file

import time
import asyncio

def timer(func):
    if asyncio.iscoroutinefunction(func):
        async def wrapper(*args, **kwargs):
            start = time.time()
            await func(*args, **kwargs)
            elapsed = time.time() - start
            print(f"Elapsed Time: {elapsed}")
        return wrapper

async def coroutine(name, delay):
    print(f"running coroutine: {name}")
    await asyncio.sleep(delay)
    print(f"finished  coroutine: {name}")

@timer
async def main():
    task1 = asyncio.create_task(coro=coroutine("Read Sensors", 2))
    task2 = asyncio.create_task(coro=coroutine("Health Check", 2))

    print("Both tasks started")
    await(task1)
    await(task2)
    print("Both tasks completed")

if __name__ == "__main__":
    asyncio.run(main())
