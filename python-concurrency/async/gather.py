# True parallel execution unlike task based execution.
import time
import asyncio

async def function1():
    await asyncio.sleep(1)
    print("function 1")
    return "I"

async def function2():
    await asyncio.sleep(1)
    print("function 2")
    return "am"

async def function3():
    await asyncio.sleep(4) 
    print("function 3")
    return "batman"

async def main():
    """
    using the gather method from asyncio to have structured execution
    """
    gathered_functions = await asyncio.gather(
        function1(),
        function2(),
        function3()
    )
    print(gathered_functions)

start = time.time()
asyncio.run(main())
end = time.time()
print("asyncio execution time: {:.2f} seconds".format(end - start))


'''
Output:
- change in execution order visible
- 1s faster than the task based asyncio and 2s faster than the synchronous execution

function 1
function 2
function 3
['I', 'am', 'batman']
asyncio execution time: 4.02 seconds
'''