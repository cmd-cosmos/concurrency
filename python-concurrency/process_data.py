# sharing data among multiple processes by using array and values

# same problem as seen in the multi3 file ---> appending to the results array from a child process

# Using the Array element from multiprocessing module for shared data.

import time
import multiprocessing

# result = [] ---> remove the global results array

def foo(nums:list,results:list):
    """function to square the entries of nums array"""

    print("foo process started")
    for idx,num in enumerate(nums):
        results[idx] = num**2
        print("square of {} = {}".format(num,num**2))
    print("foo process ends.")

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    n = len(nums)
    results = multiprocessing.Array('i',n) # inbuilt Array --> shared memory.
    p = multiprocessing.Process(target=foo, args=(nums,results)) 

    p.start()
    p.join()

    print("main scope results array = {}".format(results[:]))


