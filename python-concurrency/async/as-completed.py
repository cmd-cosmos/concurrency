#### using task functions like gather, wait and as_completed
import random

import asyncio
import time

async def coroutine(num):
    ''' coroutine to square num '''
    time.sleep(1)
    return num**2

async def main(coroutine_list):
    ''' main coroutine '''
    for futures in asyncio.as_completed(coroutine_list):
        print(await futures)

coroutine_list = [coroutine(random.randint(1,100)) for i in range(5)]

start = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(coroutine_list))
loop.close()
end = time.time()
exe_time = end - start
print("closed execution loop - time: {:.3f} seconds".format(exe_time))

#--------------------------------------------------------------------------#

def synchronous_coroutine(num):
    ''' coroutine to square num '''
    time.sleep(1)
    return num**2

t1 = time.time()
for i in range(5):
    print(synchronous_coroutine(random.randint(1,100)))
t2 = time.time()
print("Synchronous execution time: {} seconds".format(t2-t1))

'''
Output:
### time delta would be more significant for more complex operations.

1024
9216
484
3364
1369
closed execution loop - time: 5.005 seconds

2601
6889
3721
4096
6084
Synchronous execution time: 5.006121397018433 seconds
'''