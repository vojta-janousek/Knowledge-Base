'''
Output: Final state: 0, Elapsed time: 2.560312032699585s
'''
import time


def producer():
    global number
    number += 1


def consumer():
    global number
    number -= 1


if (__name__ == '__main__'):
    start = time.time()
    limit = 10000000
    global number
    number = 0

    for i in range(limit):
        producer()
        consumer()

    end = time.time()

    print('Final state: {}, Elapsed time: {}s'. format(number, end - start))
