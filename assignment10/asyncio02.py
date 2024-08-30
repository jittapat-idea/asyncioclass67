# example of using an asyncio queue without blocking
from random import random
import asyncio
import time
 
# coroutine to generate work
async def producer(queue):
    print('Producer: Running')
    start_producer = time.perf_counter()
    # generate work
    for i in range(10):
        # generate a value
        value = i
        # block to simulate work
        sleeptime = 1 #random() 0.3, 0.5, 0.8, 1, 1.5
        print(f"> Producer {value} sleep {sleeptime}")
        await asyncio.sleep(sleeptime)
        # add to the queue
        print(f"> Producer put {value}")
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    print('Producer: Done')
    time_complete = time.perf_counter() - start_producer
    print(f"Producer Time : {time_complete} seconds")
 
# coroutine to consume work
async def consumer(queue):
    print('Consumer: Running')
    # consume work
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print('Consumer: got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')
    # all done
    print('Consumer: Done')
 
# entry point coroutine
async def main():
    # create the shared queue
    start_time = time.perf_counter()
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))
    end_time = time.perf_counter()
    print(f"Time taken: {end_time-start_time} seconds")
 
# start the asyncio program
asyncio.run(main())