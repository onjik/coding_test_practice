# 하루 한곳에서만 강연을 할 수 있다
# 첫째날 갈 수 있는 곳 중에서 가장 많이 벌수 있는 곳을 간다?
# 아니다. 맨 마지막 갈 수 있는 곳부터 계산을 해야한다
# 맨 마지막 날 부터
# 갈 수 있는 가장 많이 버는 곳을 따져야한다.
# 최대 힙 큐를 사용해야겠다
# 최대 힙에 맨 마지막 날 부터 가능 한 것을 쭉 다 박은다음에
# 각 날짜 별로 가능한 가장 비싼 것을 가면 될 것 같다

from heapq import heappush, heappop
from collections import deque

# input
n = int(input())
if n == 0:
    print(0)
    exit()
lec = [tuple(map(int, input().split())) for _ in range(n)]  # 가격, 날짜 순서
lec.sort(reverse=True,key=lambda x:(x[1],x[0]))  # 1. 날짜가 큰 순, 2. 가격이 높은 순
lec = deque(lec)
max_day = lec[0][1]
result = 0
tmp = []
for day in range(max_day, 0, -1):
    while lec and lec[0][1] >= day:
        heappush(tmp, -lec[0][0])  # 가격 넣기
        lec.popleft()
    if tmp:
        result -= heappop(tmp)
print(result)