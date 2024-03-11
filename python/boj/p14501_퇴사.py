# 백트래킹 행위는 뽑고, 안뽑고
# 가장 최근의 녀석이 상담 종료 여부를 체크하고
# 남아있는 날짜를 체크해서, 가능한지 체크하고,
# 맨 끝 날짜 까지 가면, 금액을 업데이트 하자

def dfs(idx, time_left, price_total):
    global ans
    if idx == N:
        ans = max(ans, price_total)
        return
    if time_left != 0:
        # 아직 이전 상담이 안끝났다.
        return dfs(idx + 1, time_left - 1, price_total)

    # 오늘 날짜의 상담 정보
    duration, price = c[idx]

    # 가능 여부 체크
    if duration > N - idx:
        return dfs(idx + 1, time_left, price_total)

    # 뽑고, 안뽑고 백트래킹
    dfs(idx + 1, time_left + duration -1, price_total + price)
    dfs(idx + 1, time_left, price_total)


# input
N = int(input())
c = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# call
dfs(0, 0, 0)

print(ans)