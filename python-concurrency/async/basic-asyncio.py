# using asyncio with the same program execution flow as the synchronous code to speed up execution
# helps in making iobound processes faster by asynchronous execution.

import time
import asyncio

# all functions marked as async
# if async kw used with functions then await must be used.

async def function1():
    await asyncio.sleep(1)
    print("function 1")

async def function2():
    await asyncio.sleep(1)
    print("function 2")

async def function3():
    await asyncio.sleep(4) 
    print("function 3")

# creating a main task execution function that awaits for function completion

async def main():
    # creating tasks makes sure that the function passed to the task is executed when 
    task = asyncio.create_task(function1())
    # await function1()
    await function2()
    await function3()


start = time.time()
asyncio.run(main())
end = time.time()
print("asyncio execution time: {:.2f} seconds".format(end - start))


'''
Output:

function 2
function 1
function 3
asyncio execution time: 5.04 seconds

'''

'''
function2() --> starts immediately and pauses for 1 second due to await asyncio.sleep(1).

function1() --> doesn't start until the event loop processes it, processed while function2() is waiting. scheduled to execute in the future using create_task().

function3() --> starts after function2() completes and function1() runs, as it's awaited last in line.

Queue: [2,1,3] 
---> 1 is scheduled to run when we get time so we go to next function in queue
---> so 2 runs 1st and goes into asyncio await sleep for 1 second
---> now func1 is run as func 2 is sleeping and func 1 goes to sleep
---> now func2 is done and prints its output, func3 timer started
---> func1 is also done sleeping and prints to console
---> now func3 wakes up and prints at last
'''