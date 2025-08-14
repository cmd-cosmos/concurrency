# using locks to prevent race condition in the same throttle up and down example

import time
import multiprocessing

def throttle_up(throttle_value, lock):
    """child process that increases shared throttle value"""
    print("throttle up process called\n")
    for i in range(100):
        time.sleep(0.01)
        # start of critical section
        lock.acquire()
        throttle_value.value += 1
        lock.release()
        # end of critical section
    print("throttle up process killed\n")

def throttle_down(throttle_value, lock):
    """child process that decreases shared throttle value"""
    print("throttle down process called\n")
    for i in range(100):
        time.sleep(0.01)
        # start of critical section
        lock.acquire()
        throttle_value.value -= 1
        lock.release()
        # end of critical section
    print("throttle down process killed\n")

if __name__ == "__main__":
    throttle_value = multiprocessing.Value('i',50)
    
    lock = multiprocessing.Lock()   # Lock class implemented to avoid race conditions

    t_up = multiprocessing.Process(target=throttle_up, args=(throttle_value,lock))
    t_down = multiprocessing.Process(target=throttle_down, args=(throttle_value,lock))

    t_up.start()
    t_down.start()

    t_up.join()
    t_down.join()

    print(throttle_value.value)     # output is fixed to 50 now as both processes cancel each others modifications
