from concurrent.futures import ThreadPoolExecutor
import threading

# very helpful for I/O bound tasks

def sum_sensor_vals():
    print("Executing: sensor val summation task.\n")
    pressure = [i for i in range(20)]
    result = 0
    for val in pressure:
        result += val
    print("sum = {}\n".format(result))
    print("Executed by: {}\n".format(threading.current_thread())) # thread that completed execution
    return result

def main():

    # a maximum of 3 threads performing concurrent execution
    executor = ThreadPoolExecutor(max_workers=3)
    task1 = executor.submit(sum_sensor_vals)
    task2 = executor.submit(sum_sensor_vals)
    task3 = executor.submit(sum_sensor_vals)

    # can also be used as a context manager
    with ThreadPoolExecutor(max_workers=3) as executor_cm:
        task1 = executor_cm.submit(sum_sensor_vals)
        task2 = executor_cm.submit(sum_sensor_vals)
        task3 = executor_cm.submit(sum_sensor_vals)
        
        # retrieves results if function returns
        print(f"task 1 result: {task1.result()}")
        print(f"task 2 result: {task2.result()}")
        print(f"task 3 result: {task3.result()}")

if __name__ == "__main__":
    main()

'''
Output for regular thread pool executor use:

Executing: sensor val summation task.

sum = 190
Executing: sensor val summation task.


Executed by: <Thread(ThreadPoolExecutor-0_0, started 24204)>
sum = 190


Executing: sensor val summation task.
Executed by: <Thread(ThreadPoolExecutor-0_1, started 26444)>


sum = 190

Executed by: <Thread(ThreadPoolExecutor-0_2, started 48224)>
'''


'''
Output for using threadpool executor as context manager:

Executing: sensor val summation task.

sum = 190
Executing: sensor val summation task.
Executing: sensor val summation task.

sum = 190



sum = 190
Executed by: <Thread(ThreadPoolExecutor-0_0, started 8536)>
Executed by: <Thread(ThreadPoolExecutor-0_1, started 26444)>



Executed by: <Thread(ThreadPoolExecutor-0_2, started 49896)>
task 1 result: 190

task 2 result: 190
task 3 result: 190
'''