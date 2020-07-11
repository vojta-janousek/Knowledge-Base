'''
Output: -1000000 1000000 Elapsed time: 145.15557622909546
'''
import time

from multiprocessing import Process, Lock


def producer(n):
    for i in range(n):
        global _lock
        _lock.acquire()
        with open('number_file.txt', 'r+') as f:
            inc_value = int(f.read()) + 1
            f.seek(0)
            f.truncate()
            f.write(str(inc_value))

        _lock.release()
        print(inc_value)


def consumer(m):
    for j in range(m):
        global _lock
        _lock.acquire()
        with open('number_file.txt', 'r+') as g:
            dec_value = int(g.read()) - 1
            g.seek(0)
            g.truncate()
            g.write(str(dec_value))

        _lock.release()
        print(dec_value)


if (__name__ == '__main__'):
    start = time.time()
    limit = 30
    global _lock
    _lock = Lock()

    produce_process = Process(target=producer, args=(limit,))
    consume_process = Process(target=consumer, args=(limit,))
    produce_process.start()
    consume_process.start()
    produce_process.join()
    consume_process.join()

    print('Elapsed time: {}'.format(time.time() - start))
