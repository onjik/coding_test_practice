# 1번 부터 N번까지 단방향 도로
# 모든 거리 1
# x로 부터 거리가 k인 모든 도시들의 번호를 출력하시오

# visited 체크도 하고
# 그렇다면 이건 bfs네 그냥

from collections import deque

n, m, k, x = map(int, input().split())
link = [tuple(map(int, input().split())) for _ in range(m)]

visited = [False] * (n + 1)
visited[x] = True

q = deque()
q.append(x)
step = 0
while q:
    # 동일 거리의 후보들 다 돌기
    for _ in range(len(q)):
        v = q.popleft()
        # 여기서 갈 수 있는 녀석들 다 큐에 넣기
        for l in link:
            if l[0] != v:
                continue
            if visited[l[1]]:
                continue
            visited[l[1]] = True
            q.append(l[1])
    step += 1  # 현재 큐에 들어잇는게
    if step == k:
        break
if len(q) == 0:
    print(-1)
q = list(q)
q.sort()
for v in q:
    print(v)

