# using the cancel() function to cancel all upcoming tasks.
# tasks change state from pending to cancelling if all tasks used for cancellation

import asyncio
import time

async def task():
    time.sleep(1)
    print('Flight Activaation Process')

    for task in asyncio.all_tasks():
        print(task)
        task.cancel()
        print(task)

async def main():
    for i in range(5):
        asyncio.ensure_future(task())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
print("Loop Closed")

