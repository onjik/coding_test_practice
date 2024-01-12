# 각각의
# D : 두배
# S : -1
# L : 왼편으로 회전
# R : 오른편으로 회전
# 숫자는 int형으로 저장해서 빠르게
# 연산 가지치기는 shift, 두배, -1순으로
# 최소한의 명령어

from collections import deque
def bfs(a, b):
    q = deque()
    visited = [False] * 10000
    q.append((a, ''))

    while q:
        cur = q.popleft()
        num = cur[0]
        path = cur[1]

        if num == b:
            return path
        d = num * 2 % 10000
        if not visited[d]:
            visited[d] = True
            q.append((d,path + 'D'))
        s = (num - 1) % 10000
        if not visited[s]:
            visited[d] = True
            q.append((s,path+'S'))
        l = num // 1000 + (num % 1000)*10
        if not visited[l]:
            visited[l] = True
            q.append((l,path+'L'))
        r = num // 10 + (num % 10) * 1000
        if not visited[r]:
            visited[r] = True
            q.append((r,path+'R'))


# input
N = int(input())

for _ in range(N):
    A, B = map(int, input().split())
    print(bfs(A, B))
