#pylint: skip-file
#type: ignore

# UNOPTIMIZED PORT SCANNER

import time
from socket import AF_INET, SOCK_STREAM, socket

def testPortNum(host, port):
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.settimeout(0.5)
        try:
            sock.connect((host, port))
            return True
        except:
            return False

def portScanner(host, ports):
    print(f"Scanning {host}...")
    for port in ports:
        if testPortNum(host=host, port=port):
            print(f"> {host} : {port} open")

if __name__ == "__main__":
    host = "python.org"
    ports = range(1024)
    
    t1 = time.time()
    portScanner(host=host, ports=ports)
    t2 = time.time()
    del_t = t2 - t1
    print(f"Time Elapsed: {del_t:.5f}s")
