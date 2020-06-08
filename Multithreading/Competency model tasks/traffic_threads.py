import threading
import time


def producer(n):
    for i in range(n):
        mutex.acquire()
        global number
        number += 1
        mutex.release()


def consumer(m):
    for j in range(m):
        mutex.acquire()
        global number
        number -= 1
        mutex.release()


if (__name__ == '__main__'):
    limit = 10000000
    global number
    number = 0

    mutex = threading.Lock()

    one = threading.Thread(target=producer, args=(limit,))
    one.start()
    two = threading.Thread(target=consumer, args=(limit,))
    two.start()
    one.join()
    two.join()

    print(number)
