from queue import PriorityQueue
import sys

n = int(sys.stdin.readline())
queue = PriorityQueue()
result = []

for _ in range(n):
    x = int(sys.stdin.readline())
    result.append(x)
    
    if x == 0:
        if queue.empty():
            print(0)
        else:
            print(queue.get())
    else:
        queue.put(x)
