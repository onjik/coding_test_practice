# bfs 로 접근하자

from collections import deque

MAX = 10e9

# input
s, t = map(int, input().split())
if s == t:
    print(0)
    exit()

q = deque()
visited = set()

q.append((s, ""))
visited.add(s)

while q:
    n, path = q.popleft()

    if n == t:
        print(path)
        exit()

    nn = n * n
    if 0 <= nn <= MAX and nn not in visited:
        q.append((nn, path + "*"))
        visited.add(nn)
    nn = n + n
    if 0 <= nn <= MAX and nn not in visited:
        q.append((nn, path + "+"))
        visited.add(nn)
    nn = 1
    if 0 <= nn <= MAX and nn not in visited:
        q.append((nn, path + "/"))
        visited.add(nn)

print(-1)