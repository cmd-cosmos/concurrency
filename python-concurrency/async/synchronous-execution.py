# slow synchronous execution.
# inherent to python generic execution flow

import time
import asyncio # asyncio not used.

def function1():
    time.sleep(1)
    print("function 1")

def function2():
    time.sleep(1)
    print("function 2")

def function3():
    time.sleep(1)
    print("function 3")


# concurrent execution
start = time.time()
function1()
function2()
function3()
end = time.time()
print("synchronous execution time: {:.2f} seconds".format(end - start))

'''
Output:

function 1
function 2
function 3
synchronous execution time: 3.00 seconds

'''