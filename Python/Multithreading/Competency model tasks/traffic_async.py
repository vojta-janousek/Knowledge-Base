'''
Output: Final state: 0, Elapsed time: 1.4552998542785645s
'''
import time
import asyncio


async def producer(n):
    for i in range(n):
        global number
        number += 1


async def consumer(m):
    for j in range(m):
        global number
        number -= 1


async def run_traffic(k):
    produce = asyncio.create_task(producer(k))
    consume = asyncio.create_task(consumer(k))
    await produce
    await consume


if (__name__ == '__main__'):
    start = time.time()
    limit = 10000000
    global number
    number = 0

    asyncio.run(run_traffic(limit))

    end = time.time()

    print('Final state: {}, Elapsed time: {}s'.format(number, end - start))
