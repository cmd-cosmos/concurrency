# asyncio semaphores and bounded semaphores
# prevents overuse of resources
# semaphores have an internal counter that is incremented and decremented whenever either an acquire or a release call is made.

import asyncio


async def worker(semaphore):
    await semaphore.acquire()
    print("Semaphore Acquired")
    await asyncio.sleep(1) # simulating task being performed
    print("Releasing Semaphore")
    semaphore.release()

async def main(loop):
    semaphore = asyncio.Semaphore(value=2)
    task1 = asyncio.create_task(worker(semaphore=semaphore))
    task2 = asyncio.create_task(worker(semaphore=semaphore))
    task3 = asyncio.create_task(worker(semaphore=semaphore))
    await asyncio.wait([task1, task2, task3])
    print("main coroutine execution")

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
print("All workers returned")
loop.close()
print("Event loop closed")

'''
Output:

Semaphore Acquired
Semaphore Acquired
Releasing Semaphore
Releasing Semaphore
Semaphore Acquired
Releasing Semaphore
main coroutine execution
All workers returned
Event loop closed

'''


### Bounded Semaphore: does not allow more releases than acquires
### equal releases and acquires