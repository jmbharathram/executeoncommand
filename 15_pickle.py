'''
Pickle / Unpickle
- helps you to serialize/deserialize objects or data structures
- Serialization is the process of converting an object state into a format that can be saved into a file or memory.
- can be used as cache
- support many object types but there are limitations (Database connections, lambda, threads etc.)
- dump/dumps and load/loads
'''

import time
import pickle
import os

def generate_even_squares(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num*num)
            
    return even_list

t1 = time.time()

if os.path.exists("even.pickle"):
  file = open('even.pickle', 'rb')
  even_squares = pickle.load(file)
  file.close()
else:
  even_squares = generate_even_squares(range(30000000))
  file = open('even.pickle', 'wb')
  pickle.dump(even_squares, file)
  file.close()

print(even_squares[:20])

t2 = time.time()
time_diff = t2 - t1

print(round(time_diff,1), "secs")
