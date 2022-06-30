import asyncio
import time

# async def part1(n):
#     print("This is part 1 before sleep",n)
#     n = await part2(n)
#     print("This is part 1 after sleep",n)
#     return n

# async def part2(n):
#     print("This is part 2 before sleep",n)
#     n = n**2
#     # await asyncio.sleep(n)
#     # print("This is part 2 after sleep",n)
#     return n

# async def chain(n):
#     #start = time.perf_counter()
#     print("in chain ",n)
#     p1 = await part1(n)
#     #p2 = await part2(n)
#     #end = time.perf_counter() - start
#     #print("Time to execute the program ",end)


# async def main():
#     start = time.perf_counter()
#     res = await asyncio.gather(*(chain(i) for i in range(1,4)))
#     end = time.perf_counter() - start
#     print("total time of execution ",end)
#     return res

# asyncio.run(main())

async def execute(delay,value):
    await asyncio.sleep(delay)
    print(value)

async def hello():
    start = time.perf_counter()
    print("Waiting fo 5 seconds.")
    # for _ in range(5):
    #     await asyncio.sleep(1)
    #     print("hello")
    task1 = asyncio.gather(execute(1,"dilshad"))
    task2 = asyncio.gather(execute(2,"khan"))

    await task1
    await task2
    print("Finish waiting")
    end = time.perf_counter() - start
    print("time ",end)
asyncio.run(hello())