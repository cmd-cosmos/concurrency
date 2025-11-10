#pylint: skip-file

import asyncio

async def coroutine(name, delay):
    print(f"running coroutine: {name}")
    await asyncio.sleep(delay)
    print(f"finished  coroutine: {name}")

async def main():
    task1 = asyncio.create_task(coro=coroutine("Read Sensors", 2))
    task2 = asyncio.create_task(coro=coroutine("Health Check", 2))

    print("Both tasks started")
    await(task1)
    await(task2)
    print("Both tasks completed")

if __name__ == "__main__":
    asyncio.run(main())
