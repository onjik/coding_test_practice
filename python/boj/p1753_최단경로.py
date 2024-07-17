# 최단 경로
# 방향 그래프
# 시작 점에서 다른 모든 정점으로 최단 경로 -> 다익스트라 아니면 워셜
# 30만 n ** 3 이면 대략 10^15
# 다익스트라로 가자

# 다익스트라 -> 최소 신장 트리와 비슷하나, 우선순위가 현재까지 길이 포함해서 결정

# visited, heapq 사용 하자
# 정점 번호는 1부터 시작

# input
V, e = map(int, input().split())
start = int(input())

# 딕셔너리로 미리 인덱싱 해놓자
# list of (거리, 목적지)
edges = dict()
for i in range(V + 1):
    edges[i] = []

for _ in range(e):
    u, v, w = map(int, input().split())
    edges[u].append((w, v,))

# visited, q 초기화
import heapq

visited = [False] * (V + 1)
q = []

visited[start] = True
for edge in edges[start]:
    heapq.heappush(q, edge)

answer = [-1] * (V + 1)
answer[start] = 0

# 알고리즘 시작
while q:
    # 가장 가까운 녀석 뽑기
    dist, dest = heapq.heappop(q)
    if visited[dest]:
        continue

    # 방문 처리
    visited[dest] = True
    answer[dest] = dist

    # 여기서 이어지는 곳들 전부 넣기
    for e_dist, e_dest in edges[dest]:
        if visited[e_dest]:
            continue
        heapq.heappush(q, (e_dist + dist, e_dest,))

for no in range(1, V + 1):
    if answer[no] == -1:
        print("INF")
    else:
        print(answer[no])