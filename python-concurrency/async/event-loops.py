# event loops in the asyncio library
# running an event loop for indefinite time/ till a condition is fulfilled.

import asyncio

async def coroutine():
    while True:
        await asyncio.sleep(1)
        print('Comms Loop open..')

async def coroutine2():
    while True:
        await asyncio.sleep(1)
        print('Comms state check..')


# loop = asyncio.get_event_loop()
# try:
#     loop.run_until_complete(coroutine())
# finally:
#     loop.close()

# running loop indefinitely

loop2 = asyncio.get_event_loop()
try:
    asyncio.ensure_future(coroutine())
    asyncio.ensure_future(coroutine2())
    loop2.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing loop...")
    loop2.close()


