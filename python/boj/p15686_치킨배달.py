# N * N 크기
# 빈칸 치킨집 집
# r, c 는 1부터 시작
# 치킨 거리 : 치킨집까지 최단 거리
# 도시의 치킨 거리 : 모든 집의 치킨 거리의 합
# 거리 구하는 공식
# 각 속성의 차이값 합

# m개만 남길때, 도시의 치킨 거리가 작게 하려면?

# N이 굉장히 작다
# 치킨집도 13보다 작다
# 집도 굉장히 작다

# 단순 반복으로 풀리나?
# 각각 거리를 다 구할 때 100 * 13

# 가능할 듯?
# 구현 문제인듯
from itertools import combinations

MAX = int(1e9)


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 각각의 집하고, 치킨집의 인덱스를 구하자
houses = []
chickens = []
for y in range(n):
    for x in range(n):
        v = board[y][x]
        if v == 0:
            continue
        elif v == 1:
            houses.append([x, y])
        elif v == 2:
            chickens.append([x, y])
chicken_cnt = len(chickens)
house_cnt = len(houses)

# 그다음 최소 거리 맵을 만든다.
distance = [[MAX] * chicken_cnt for _ in range(house_cnt)]
for hi, house in enumerate(houses):
    for ci, chicken in enumerate(chickens):
        # 거리 계산
        distance[hi][ci] = dist(house, chicken)

city_dis = MAX
for chicken_idxs in combinations(range(chicken_cnt), m):
    # 각각의 집 마다
    ans = 0
    for h_i in range(house_cnt):
        min_value = MAX
        for c_i in chicken_idxs:
            min_value = min(min_value, distance[h_i][c_i])
        ans += min_value
    city_dis = min(city_dis, ans)
print(city_dis)