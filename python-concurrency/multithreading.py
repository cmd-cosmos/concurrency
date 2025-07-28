# more practice on multithreading

import threading
import time


nums: list = [1,2,3,4,5]

def sq_fn(nums: list):
    for num in nums:
        time.sleep(0.02)
        print("Square of {} = {}\n".format(num,num**2))

def cube_fn(nums: list):
    for num in nums:
        time.sleep(0.02)
        print("Cube of {} = {}\n".format(num,num**3))

start = time.time_ns()

# calling functions synchronously ---> time delta = 248290200
# sq_fn(nums)
# cube_fn(nums) 

t1 = threading.Thread(target=sq_fn,args=(nums,))
t2 = threading.Thread(target=cube_fn,args=(nums,))

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time_ns()
delta = end - start

# The GIL is a hinderence to levaraging all multithreading advantages.
# when the functions are called using spearate threads
# execution time reduced by half 
# time delta value ---> 107811000

print("Completion time = {}".format(delta))



