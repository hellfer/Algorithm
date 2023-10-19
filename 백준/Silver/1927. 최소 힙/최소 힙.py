import heapq
import sys

n = int(sys.stdin.readline())
result = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if not result:  # result가 비어있으면
            print(0)
        else:
            print(heapq.heappop(result))
    else:
        heapq.heappush(result, x)
