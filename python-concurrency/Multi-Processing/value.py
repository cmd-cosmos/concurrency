# using Value class to manipulate a single value shared among the parent and child process.

import multiprocessing

def foo(val):
    """function to update value from the parent process"""

    print("foo process started")
    val.value = 3.1415
    print("foo process ends, value updated.")

if __name__ == "__main__":
    val = multiprocessing.Value('d',2.718)  # updating e to pi using foo
    print("val value before updating = {}".format(val.value))
    p = multiprocessing.Process(target=foo, args=(val,)) 

    p.start()
    p.join()

    print("updated value updated by foo = {}".format(val.value))
