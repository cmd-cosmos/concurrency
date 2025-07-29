# using Queue to share data between processes
# for IPC either File, shared memory or a message pipe can be deployed
# Queue falls under the shared memory type

import multiprocessing

def format_q(q):
    lst = []
    while q.empty() is False:
        lst.append(str(q.get()))
    return lst

def foo(nums,q):
    """child process that calculates square of all elements in nums list"""

    print("child process foo started")
    print("Updating the q passed by the parent process")

    for num in nums:
        q.put(num**2)

    print("child process foo killed, returned updated q")

if __name__ == "__main__":
    nums  = [1,2,3,4,5]
    q = multiprocessing.Queue()
    p = multiprocessing.Process(target=foo, args=(nums,q))
    p.start()
    p.join()
    q_formatted = ",".join(format_q(q))
    print("q in main process updated to: {}".format(q_formatted))

