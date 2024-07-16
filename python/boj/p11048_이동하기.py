# 이동하기
# N * M 체스판
# 1,1 ~ N,M
# 동 남 남동 이동
# 가져올 수 있는 최대 사탕 갯수

# 전형적인 DP 인듯

# dp = 현재 위치 까지 먹을 수 있는 최대 사탕 갯수

n, m = map(int, input().split())
board = [list(map(int, input().spit())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]

# 초기값 설정
dp[0][0] = board[0][0]
for col in range(1, n):
    dp[0][col] = dp[0][col - 1] + board[0][col]

for row in range(1, n):
    dp[row][0] = dp[row - 1][0] + board[row][0]

# 나머지 dp 채우기
for row in range(1, m):
    for col in range(1, n):
        dp[row][col] = max(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1]) + board[row][col]

# 결과값 리턴
print(dp[m - 1][n - 1])