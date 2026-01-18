#pylint: skip-file

import time
from concurrent.futures import ThreadPoolExecutor

def fetch(id):
    print("Task {}: STARTING".format(id))
    time.sleep(2)
    print("Task {}: FINISHED".format(id))
    return "Result: {}".format(id)

start = time.time()
with ThreadPoolExecutor(max_workers=5) as exec:
    futures = []
    for i in range(5):
        futures.append(exec.submit(fetch, i))
    res = [fut.result() for fut in futures]
end = time.time()

print("RESULTS: {}".format(res))
print("TIME: {:.5f} seconds".format(end - start))
    
