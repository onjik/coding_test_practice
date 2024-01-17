# bfs로 풀자

import sys
from collections import deque

input = sys.stdin.readline

A, B, C = map(int, input().split())

total = A + B + C
if total % 3 != 0:
    print(0)
    exit()

# bfs
q = deque()
visited = [[False] * total for _ in range(total)]

max_e = max(A, B, C)
min_e = min(A, B, C)
q.append((max_e, min_e))
visited[max_e][min_e] = True
while q:
    x, y = q.popleft()
    z = total - (x + y)
    if x == y == z:
        print(1)
        exit()
    for i, j in (x, y), (y, z), (z, x):
        if i == j:
            continue
        if i > j:
            i, j = i - j, j + j
        else:
            i, j = i + i, j - i
        k = total - i - j

        _max = max(i, j, k)
        _min = min(i, j, k)
        if visited[_max][_min]:
            continue
        visited[_max][_min] = True
        q.append((_max, _min))
print(0)