import time
import random
import multiprocessing as mp


def printer(n, locked=True):
    if locked:
        _lock.acquire()
        print(n)
        _lock.release()
    else:
        print(n)

    # time.sleep(0.01)
    time.sleep(random.randint(1, 3))


if (__name__ == '__main__'):
    start = time.time()
    _lock = mp.Lock()
    pool = mp.Pool(2)

    for i in range(30):
        pool.apply_async(printer, [i, True])

    pool.close()
    pool.join()
    print('Elapsed time: {}'.format(time.time() - start))
