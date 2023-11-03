from collections import deque

n, m = map(int, input().split())
graph = [0 for _ in range(100001)]
visited = [0 for _ in range(100001)]

def bfs(n):
    queue = deque([n])
    visited[n] = 1

    while queue:
        x = queue.popleft()

        for nx in [x-1, x+1, x*2]:
            if 0 <= nx < 100001 and visited[nx] == 0:
                queue.append(nx)
                visited[nx] = visited[x] + 1

        if visited[m] != 0:
            break

    return visited[m] - 1

print(bfs(n))
