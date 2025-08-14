# more practice for the multiprocessing module

from multiprocessing import Process, Pool
import time
import os   

def info():
    print('module name = {}'.format(__name__))
    print('parent process = {}'.format(os.getpid()))
    print('process id = {}'.format(os.getpid()))

def foo(nums):
    """4th power of num argument list"""
    info()
    for num in nums:
        print("foo for {} = {}".format(num,num**4))

if (__name__ == "__main__"):
    print("cpu count = {}\n".format(os.cpu_count()))
    
    info()

    nums = [i for i in range(1,6)]
    
    p1 = Process(target=foo, args=(nums,))
    p2 = Process(target=foo, args=(nums,))
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
