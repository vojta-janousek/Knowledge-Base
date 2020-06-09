'''
Output: -1000000 1000000 Elapsed time: 145.15557622909546
'''
import time

from multiprocessing import Process


def producer():
    for i in range(1000000):
        with open('number_file.txt', 'r+') as f:
            inc_value = int(f.read()) + 1
            f.seek(0)
            f.write(str(inc_value))

    print(inc_value)


def consumer():
    for j in range(1000000):
        with open('number_file2.txt', 'r+') as g:
            dec_value = int(g.read()) - 1
            g.seek(0)
            g.write(str(dec_value))

    print(dec_value)


if (__name__ == '__main__'):
    start = time.time()

    produce_process = Process(target=producer)
    consume_process = Process(target=consumer)
    produce_process.start()
    consume_process.start()
    produce_process.join()
    consume_process.join()

    end = time.time()

    print('Elapsed time: ', str(end - start))
