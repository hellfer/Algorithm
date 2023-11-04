from collections import deque

def bfs():
    q = deque()
    q.append(n)
    time[n] = 0
    cnt[n] = 1

    while q:
        x = q.popleft()
        for nx in (x-1, x+1, x*2):
            if 0 <= nx < 100001:
                if time[nx] == -1:
                    time[nx] = time[x] + 1
                    cnt[nx] = cnt[x]
                    q.append(nx)
                elif time[nx] == time[x] + 1:
                    cnt[nx] += cnt[x]

n, k = map(int, input().split())
time = [-1]*100001
cnt = [0]*100001

bfs()

print(time[k])
print(cnt[k])





