# 파일 합치기
# 각 챕터 별로 파일 나눠 저장 -> 나중에 합치기
# 두개씩 합쳐나가기
# 합치는 비용 = 두 파일의 크기의 합

# 먼저 합칠 수록 여러번 더하게 된다?
# 아니다 어떤 조합으로 더할지 모른다 -> 그리디 아니다

# 최소 비용 구하라

# 아 연속이구나?
# 행렬의 연산 횟수 문제와 같다

# dp(i, j) : i번 째 부터 j 번째 까지 합칠 때 드는 최소 비용
# dp(i, j) = dp(i, k) + dp(k, j) + sum(i, k) + sum(k, j) for k
# 그니까 양쪽 의 최소 비용 + 병합 비용
# 병합 비용의 경우 고정값이다. 따라서 dp(i, k) + dp(k, j)의 최솟값을 찾는 문제다.

# dp[x,x]는 모두 0으로 초기화
# 메모이제이션으로 하자

t = int(input())


def solution(n: int, sizes: list[int]):
    # dp 테이블 초기화
    dp = [[-1] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for i in range(n - 1):
        dp[i][i + 1] = sizes[i] + sizes[i + 1]

    # 그다음 이제 재귀 호출
    def dfs(start, end):
        if dp[start][end] != -1:
            return dp[start][end]

        min_val = int(1e9)  # INF
        for k in range(start, end):
            min_val = min(min_val, dfs(start, k) + dfs(k + 1, end))


        dp[start][end] = min_val + sum(sizes[start:end + 1])
        return dp[start][end]

    # 맨 끝에서 끝까지 재귀호출
    result = dfs(0, n - 1)
    return result


for _ in range(t):
    n = int(input())
    sizes = list(map(int, input().split()))
    print(solution(n, sizes))