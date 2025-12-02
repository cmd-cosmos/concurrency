#pylint: skip-file
#type: ignore

# each thread in a pool is called a worker
# pool is responsible for a fixed num of threads

from concurrent.futures import ThreadPoolExecutor
import threading
import requests

def fetch(url):
    id = threading.get_ident()
    name = threading.current_thread().name
    print(f"Thread Name: {name} | Thread id: {id:5} | Fetching: {url}\n")
    r = requests.get(url=url)
    return len(r.text)

url_lst = [
    "https://www.spacex.com/",
    "https://www.blueorigin.com/",
    "https://rocketlabcorp.com/",
    "https://www.relativityspace.com/",
    "https://www.nasa.gov/",
    "https://www.isro.gov.in/",
    "https://www.northropgrumman.com/"
]

with ThreadPoolExecutor(max_workers=5) as executor:
    res = executor.map(fetch, url_lst)

for size in res:
    print(f"Response Size: {size}")
