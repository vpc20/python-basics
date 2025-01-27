import tracemalloc
from math import factorial

tracemalloc.start()
print(factorial(1000))
curr, peak = tracemalloc.get_traced_memory()
print(f'Current size : {curr / 1000}KB')
print(f'Peak size : {peak / 1000}KB')
tracemalloc.stop()
