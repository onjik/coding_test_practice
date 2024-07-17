# 최소 스패닝 트리
# 모든 정점 연결하면서, 거리합 최소

# 거리합만 리턴

# 다익스트라와 비슷하지만, 선택 기준이, 엣지임

# visited, deque 로 가장 짧은 거 중에 꺼내고 체크하는 식으로 가야할듯

# 양방향 간선, 정점은 1부터 시작

# input
v, e = map(int, input().split())

# 딕셔너리 형태로, 인덱싱을 미리 해두자
# (거리, 목표)
edges = dict()
for i in range(v + 1):
    edges[i] = []

# 그리고 엣지 입력 받자
for _ in range(e):
    a, b, c = map(int, input().split())
    edges[a].append((c, b,))
    edges[b].append((c, a,))

# visited, deque 초기화
import heapq

q = []
visited = [False] * (v + 1)

visited[1] = True
for elem in edges[1]:
    heapq.heappush(q, elem)

# 그 다음 순회하면서 최소 신장 트리 만들기
total_dist = 0
while q:
    # 가장 가까운 녀석 뽑기
    dist, dest = heapq.heappop(q)
    # 방문 체크
    if visited[dest]:
        continue
    # 방문 처리
    visited[dest] = True
    total_dist += dist
    # 여기서 연결된거 다 넣기
    for e_dist, e_dest in edges[dest]:
        if visited[e_dest]:
            continue
        heapq.heappush(q, (e_dist, e_dest,))

print(total_dist)