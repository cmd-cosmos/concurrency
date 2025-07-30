# using multiprocessing pool 

import multiprocessing
import time

def foo(num):
    sum = 0
    for i in range(1000):
        sum += num**2
    return sum

if __name__ == "__main__":
    nums = [i for i in range(1000000)]

# This logic will run on a single core and execute synchronously
    # results = []
    # for num in nums:
    #     results.append(foo(num))
    # print(results)

    print(multiprocessing.cpu_count())  # 16 cores available for parallel execution

# now we can divide the input among the other idle cores and aggregate the results
# we map the inputs to multiple computing units and then we reduce which is aggregate the processed values from different computing units
    start = time.time()
    p = multiprocessing.Pool()
    result = p.map(foo, nums)
    p.close()
    p.join()
    end = time.time()
    # execution time for pooled multiprocess execution
    print("Pool Execution time = {:.5f}".format(end-start)) # Execution time = 0.16 ns

    t1 = time.time()
    result = []
    for j in range(1000000):
        result.append(foo(j))
    t2 = time.time()
    print("synchronous execution time = {:.5f}".format(t2-t1))

# final performance comparision
# Pool Execution time = 7.20928     <======== significant speed when pool used
# synchronous execution time = 42.09107
