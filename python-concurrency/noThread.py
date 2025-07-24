
import threading # without threading execution times can be seen in the synchronous log
import time

start = time.time()

inp: list = [i for i in range(1,100)]

def sq(nums: list):
    sq_nums: list = [i**2 for i in nums]
    return  sq_nums

def cube(nums: list):
    cube_nums: list = [i**3 for i in nums]
    return  cube_nums

sq(inp)
time.sleep(2)
cube(inp)

stop = time.time()
time_cal = stop - start
with open("log-synchronous.txt","a") as f:
    f.write(f"Execution Time: {str(time_cal)} \n")




