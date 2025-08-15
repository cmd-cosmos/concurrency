'''
Asyncio:
- used for single threaded asynchronous execution.
- single threaded concurrent programs that utilize coroutines
- coroutines are just lightweight versions of threads
- abstracts complexity of multiplexing io over sockets
'''

import asyncio
import random

async def coroutine():
    '''
    coroutine fed to the loop.
    '''
    print("countdown sequeunce active...")

async def sensorCoroutine(id):
    DataGateheringTime =random.randint(1,5)
    await asyncio.sleep(DataGateheringTime)
    print("Coroutine {} : completed in {} seconds".format(id, DataGateheringTime))

async def main():
    '''
    event loop.
    '''
    tasks = []
    for i in range(10):
        tasks.append(asyncio.ensure_future(sensorCoroutine(i)))
    await asyncio.gather(*tasks)


    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(coroutine())
    # loop.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()