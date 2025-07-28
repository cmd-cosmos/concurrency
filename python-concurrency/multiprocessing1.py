# multiprocessing ---> preferred for CPU bound tasks
# separate instances of the GIL per core
# GIL bottleneck sort of avoided

import multiprocessing
import time

def sq_fn(nums: list):
    for num in nums:
        print("Square of {} = {}\n".format(num,num**2))

def cube_fn(nums: list):
    for num in nums:
        print("Cube of {} = {}\n".format(num,num**3))

if __name__ == "__main__":
    
    tot_cpu:int = multiprocessing.cpu_count()
    print("cpu count = {}".format(tot_cpu))
    
    array:list = [1,2,3,4,5]

    start:int = time.time_ns()

    p1 = multiprocessing.Process(target=sq_fn, args=(array,))
    p2 = multiprocessing.Process(target=cube_fn, args=(array,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end:int = time.time_ns()
    delta:int = end - start
    # time delta reduced by 10 times in comparision to multi threading
    # time delta = 82458500
    print("Execution Time = {}".format(delta))

    '''
    Output:

    cpu count = 16
    Square of 1 = 1

    Square of 2 = 4

    Square of 3 = 9

    Square of 4 = 16

    Square of 5 = 25

    Cube of 1 = 1

    Cube of 2 = 8

    Cube of 3 = 27

    Cube of 4 = 64

    Cube of 5 = 125

    Execution Time = 82458500
    '''
