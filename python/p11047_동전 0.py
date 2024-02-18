# N종류의 동전을 가지고 있고
# 수량은 무제한
# 적절히 조합해서 K 로 만드려고 한다
# 필요한 동전 갯수의 최솟값

# 그냥 큰거부터 순서대로 채우면 되나?
# 만약 배수가 된다면 맞다

# input
N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()

count = 0

for coin in coins:
    if K == 0:
        break
    # 큰 경우 건너뛰기
    if K < coin:
        continue
    # 최대 들어갈 수 있는 갯수
    n = K // coin
    count += n
    K -= coin * n

print(count)