'''
- A new thread is spawned within the existing process
- Startin a thread is faster than starting a process
- Memory is shared between all threads
- Mutexes are often necessary to control access to shared data
- One GIL (Global Interpreter Lock) for all thread
'''
import os
import math

from threading import Thread


def calculate_square():
    for i in range(10000):
        math.sqrt(i)


threads = []
for i in range(os.cpu_count()):
    print('Registering thread {}'.format(i))
    threads.append(Thread(target=calculate_square))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
