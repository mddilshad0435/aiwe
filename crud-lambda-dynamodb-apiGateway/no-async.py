import time

def part2(n):
    print("In part 2 ",n)
    n = n**2
    return n

def part1(n):
    print("In part 1 before sleep ",n)
    n = part2(n)
    print("In part1 after sleep ",n)

def chain(n):
    print("In chain ",n)
    p1 = part1(n)

def main():
    start = time.perf_counter()
    for i in range(1,4):
        chain(i)
    
    end = time.perf_counter() - start
    print("Time of execution ",end)

main()