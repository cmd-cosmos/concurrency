#type: ignore
#pylint: skip-file

import time
import asyncio

def timer(func):
    if asyncio.iscoroutinefunction(func):
        async def wrapper(*args, **kwargs):
            start = time.time()
            await func(*args, **kwargs)
            elapsed = time.time() - start
            print(f"Elapsed Time: {elapsed:.4f}s")
        return wrapper
    else:
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            elapsed = time.time() - start
            print(f"Elapsed Time: {elapsed:.4f}s")
        return wrapper
            

async def coroutine(name, delay):
    print(f"running coroutine: {name}")
    await asyncio.sleep(delay)
    print(f"finished  coroutine: {name}")

@timer
async def main():
    task1 = asyncio.create_task(coroutine("1 - I/O", 5))
    task2 = asyncio.create_task(coroutine("2 - Health Check", 3))

    print("Both async tasks started")
    await(task1)
    await(task2)
    print("Both async tasks completed")

def sync_routine(name,delay):
    print(f"running sync routine: {name}")
    time.sleep(delay)
    print(f"finished  sync routine: {name}")

@timer
def sync_main():
    print("Both sequential routines running")
    sync_routine("sync 1", 5)
    sync_routine("sync 2", 3)
    print("Both sequential routines complete")


if __name__ == "__main__":
    asyncio.run(main())

    print("*"*50)
    # running sequential routine
    sync_main()
