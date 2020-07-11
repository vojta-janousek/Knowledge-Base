'''
- A new process is started independent from the first process
- Starting a process is slow than starting a thread
- Memory is not shared between processes
- Mutexes are not necessary (unless threading in the new process)
- One GIL (Global Interpreter Lock) for each process
'''
import os
import math

from multiprocessing import Process


def calculate_square():
    for i in range(10000):
        math.sqrt(i)


processes = []
for i in range(os.cpu_count()):
    print('Registering process {}'.format(i))
    processes.append(Process(target=calculate_square))

for process in processes:
    process.start()

for process in processes:
    process.join()
