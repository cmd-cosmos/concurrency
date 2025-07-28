##### Threading - use threads for execution
#####           - great for IO bound tasks

import threading
import time

start = time.time()

sensor1: int = 1
sensor2: int = 2
sensor3: int = 3

def get_sensor_data():
    print("Pinging Sensors - get_sensor_data()")
    time.sleep(2)
    print("Sensor data received on current data collection thread.")
    print(f"Response from S1 {sensor1 + 100}")
    print(f"Response from S2 {sensor2 + 100}")
    print(f"Response from S3 {sensor3 + 100}")
    print("Sensor Data collected, previous data logged before.")

def log_previous_data():
    print("Getting sensor data on a separate thread.")
    print("logging previous data in the meantime")
    print("Flushed Sensor 1 Data: ",sensor1)
    print("Flushed Sensor 2 Data: ",sensor2)
    print("Flushed Sensor 3 Data: ",sensor3)

t1 = threading.Thread(target=get_sensor_data)
t2 = threading.Thread(target=log_previous_data)

t1.start()
t2.start()

t1.join()
t2.join()

# get_sensor_data()
# log_previous_data() 
# exe time without threading -->2.0016531944274902

end = time.time()

exe_time = end - start
print(exe_time)



