# 다익스트라 살짝 비틀어서 풀면 될듯

# input
n, m = map(int, input().split())
br = dict()
for _ in range(m):
    a,b,c = map(int, input().split())
    if a not in br:
        br[a] = []
    if b not in br:
        br[b] = []
    br[a].append((c, b))
    br[b].append((c, a))

f1, f2 = map(int, input().split())

# 요소 초기화
visited = set()
import heapq
q = []

heapq.heappush(q, (-1e9, f1))

while q:
    negative_w, cur = heapq.heappop(q)
    w = -1 * negative_w
    if cur == f2:
        print(w)
        exit()
    # 방문 처리
    if cur in visited:
        continue
    visited.add(cur)

    # 연결된 애들 다 넣기
    for bw, nn in br[cur]:
        if nn in visited:
            continue
        heapq.heappush(q, (-1 * min(bw, w), nn))

print("ERROR")