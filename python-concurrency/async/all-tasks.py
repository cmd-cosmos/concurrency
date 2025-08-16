# tasks ===> execute coroutines within an event loop
# use the futures method to declare tasks
import asyncio
import time

async def task():
    time.sleep(1)
    print("Processing Task - 1")

async def taskGenerator():
    for i in range(5):
        asyncio.ensure_future(task())
    pending = asyncio.all_tasks() # lists all tasks in the pending state before they are executed by the event loop.
    print(pending) 

# event loop for task execution
loop = asyncio.get_event_loop()
loop.run_until_complete(taskGenerator())
print("Closing Loop")
loop.close()

