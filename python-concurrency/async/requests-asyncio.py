### possible use case for asyncio ---> using requests module to download a file.

import asyncio
import time
import requests


async def function1():
    url = 'https://www.digitaltrends.com/wp-content/uploads/2023/11/starship-launch.jpeg?p=1'
    response = requests.get(url=url)
    open("StarShip1.jpeg", "wb").write(response.content)

    print("Function 1")
    return("I")

async def function2():
    url = 'https://www.digitaltrends.com/wp-content/uploads/2023/11/starship-launch.jpeg?p=1'
    response = requests.get(url=url)
    open("StarShip2.jpeg", "wb").write(response.content)

    print("Function 2")
    return("am")

async def function3():
    url = 'https://www.digitaltrends.com/wp-content/uploads/2023/11/starship-launch.jpeg?p=1'
    response = requests.get(url=url)
    open("StarShip3.jpeg", "wb").write(response.content)

    print("Function 3")
    return("Batman")

async def main():
    batch = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )

start = time.time()
asyncio.run(main=main())
end = time.time()
time_parallel = end - start
print("Time for Parallel Execution: {:.4f} seconds\n".format(time_parallel))

# creating synchronous exection for the requests

async def sync():
    # no gathering ---> synchronous execution
    await function1()
    await function2()
    await function3()

start_s = time.time()
asyncio.run(main=sync())
end_s = time.time()
sync_exe_time = end_s - start_s
print("Time for Synchronous Execution: {:.4f} seconds\n".format(sync_exe_time))

'''
Output:
- since files are 300kb the difference is not much, but the difference will scale up as io heavy tasks are assigned to the functions
- asyncio is 300ns faster here

Function 1
Function 2
Function 3
Time for Parallel Execution: 0.2594 seconds

Function 1
Function 2
Function 3
Time for Synchronous Execution: 0.2857 seconds
'''