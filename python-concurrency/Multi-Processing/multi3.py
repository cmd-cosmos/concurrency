# seeing difference in address spaces using a global and a local results array.
# the process append command will not append the global results array as the process will make its own separate copy in its own address space.

import time
import multiprocessing

results = []    # scope = main

def foo(nums:list):
    """function to square the entries of nums array"""
    print("foo process started")
    global results  # scope will be foo address space
    for num in nums:
        print("square of {} = {}".format(num,num**2))
        results.append(num**2) # this will not affect the global results as it is a copy of the results array on line 7
    print("results array in the foo scope = {}".format(results))
    print("foo process ends.")

if __name__ == "__main__":
    nums = [1,2,3,4,5]

    p1 = multiprocessing.Process(target=foo, args=(nums,))
    p1.start()
    p1.join()

    print("results array from main scope = {}".format(results))

