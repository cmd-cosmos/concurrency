# creating race conditions by modifying shared value using 2 processes

import time
import multiprocessing

def throttle_up(throttle_value):
    """child process that increases shared throttle value"""
    print("throttle up process called\n")
    for i in range(100):
        time.sleep(0.01)
        throttle_value.value += 1
    print("throttle up process killed\n")

def throttle_down(throttle_value):
    """child process that decreases shared throttle value"""
    print("throttle down process called\n")
    for i in range(100):
        time.sleep(0.01)
        throttle_value.value -= 1
    print("throttle down process killed\n")

if __name__ == "__main__":
    throttle_value = multiprocessing.Value('i',50)
    
    t_up = multiprocessing.Process(target=throttle_up, args=(throttle_value,))
    t_down = multiprocessing.Process(target=throttle_down, args=(throttle_value,))

    t_up.start()
    t_down.start()

    t_up.join()
    t_down.join()

    print(throttle_value.value) # since no locks used, race condition observed.

