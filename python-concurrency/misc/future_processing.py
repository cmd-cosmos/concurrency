#pylint: skip-file

import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

def task(n):
    delay = random.uniform(0.5, 3.14156)
    time.sleep(delay)
    return n, delay

with ThreadPoolExecutor(max_workers=4) as exec:
    futures = [exec.submit(task, i) for i in range(10)]
    for fut in as_completed(futures):
        n, delay = fut.result()
        print("Task {} : TOOK {:.2f} seconds".format(n, delay))
