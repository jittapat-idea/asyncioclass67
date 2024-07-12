from random import random
import asyncio

# async def rice_coro(arg):
#     #generate a random value between 0 and 1
#     value = random() + 1
#     #block for a moment
#     await asyncio.sleep(value)
#     #report the value
#     print(f'>task {arg} done with {value}')


# async def noodle_coro(arg):
#     #generate a random value between 0 and 1
#     value = random() + 1
#     #block for a moment
#     await asyncio.sleep(value)
#     #report the value
#     print(f'>task {arg} done with {value}')


# async def curry_coro(arg):
#     #generate a random value between 0 and 1
#     value = random() + 1
#     #block for a moment
#     await asyncio.sleep(value)
#     #report the value
#     print(f'>task {arg} done with {value}')
foods = ['Rice','Noodle','Curry']
async def cooking(food):
    value = random()+1
    print(f'Microwave ({food}): Cooking {value} seconds...')
    #block for a moment
    await asyncio.sleep(value)
    print(f'Microwave ({food}): Finished cooking')
    return [food,value]

    

#main coroutine
async def main():
    #create many tasks
    tasks = [asyncio.create_task(cooking(i)) for i in foods ]
    #wait for all tasks to complete
    done,pending = await asyncio.wait(tasks,return_when=asyncio.FIRST_COMPLETED)
    #report results
    print(f'Completed : {len(done)}')
    task_completed = done.pop().result()
    print(f'{task_completed[0]} is completed in {task_completed[1]}')
    print(f'Uncompleted : {len(pending)}')


#start the asyncio program
asyncio.run(main())