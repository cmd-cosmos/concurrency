#pylint: skip-file

from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    time.sleep(1)
    return n**2

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, i) for i in range(100)]

t1 = time.time()
for f in futures:
    print(f"Result: {f.result()}")
t2 = time.time()
del_t = t2 - t1
print(f"Time Elapsed: {del_t:.3f}s")
