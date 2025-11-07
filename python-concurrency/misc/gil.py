#pylint: skip-file

import threading
import time

def write_file_daemon():
    with open('test.txt', 'w') as f:
        while True:
            f.write(f"log time: {time.ctime()}\n")
            f.flush()
            time.sleep(1)

def main():
    t1 = threading.Thread(target=write_file_daemon, daemon=True)
    t1.start()

    print("file write daemon started --> type 'q' to stop")

    while True:
        inp = input(">> ").strip().lower()
        if inp == 'q':
            print("terminating both threads.")
            break
    print("killing main and daemon threads.")

if __name__ == '__main__':
    main()
