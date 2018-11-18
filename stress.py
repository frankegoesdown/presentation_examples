import time
import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import cpu_count 
items = range(1000)
def call(a):
  start_time = time.time()
  r = requests.get('https://www.ozon.ru/search?text=авто')
  print("--- {} seconds --- status {}".format((time.time() - start_time), r.status_code))
with ThreadPoolExecutor(cpu_count() * 32) as executor:
  executor.map(call, items)