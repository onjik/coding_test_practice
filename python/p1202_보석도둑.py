# 가방은 작은 것 부터 선택한다
# 가방은 선택할 때, 자기 무게 이하이면서, 가격이 제일 비싼 보석을 선택한다
# 가능한 무게 중에 가장 비싼 가격을 고르는 문제이다
# Max-Heap을 사용해서 가격을 집어넣고, 꺼내면
# 지금까지 가능한 녀석중에 가장 비싼 가격을 꺼낼 수 있다.
from heapq import heappush, heappop

# Input
N, K = map(int, input().split())
gems = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

bags.sort()  # 작은 것 부터
gems.sort()  # 무게, 가격 순으로 가볍고 싼거부터
max_heap = []
result = 0
idx = 0

for bag in bags:
    # 쭉 돌면서 가능한 녀석들 다 집어넣기
    for i in range(idx, len(gems)):
        if gems[i][0] > bag:
            break
        heappush(max_heap, -gems[i][1])
        idx += 1
    if max_heap:
        result -= heappop(max_heap)
print(result)