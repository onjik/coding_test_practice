# 뒤집는 조합이 중요하지 순서는 중요하지 않다
# 그리디 알고리즘으로
# 목적 : T가 적게 나오는 것
# 비트 마스킹으로 초기 값 행을 구한다

def stob(s):
    if s == "H":
        return True
    else:
        return False


# input
N = int(input())
board = [list(map(stob, list(input()))) for _ in range(N)]

ans = N * N + 1
# n이 3일 경우
# 11 10 01 00
for bit in range(1 << N):
    tmp = [arr[:] for arr in board]
    # 비트에 맞게 행 뒤집기
    for y in range(N):
        if bit & (1 << y):
            for x in range(N):
                tmp[y][x] = not tmp[y][x]
    # 총 뒷면 갯수 세기
    t_sum = 0
    for x in range(N):
        cnt = 0
        for y in range(N):
            if tmp[y][x] == False:
                cnt += 1
        # 뒤집어서 최소값 더하기
        t_sum += min(cnt, N - cnt)
    ans = min(t_sum, ans)

print(ans)

# 배운점
# 저렇게 특정 조합을 만들때, bit를 사용하면 편리하고 메모리도 아낄 수 있다
# 행을 다 골라놓고, 열의 경우 그리디 방식으로 뒤집을지 안뒤집을지 선택하면 된다.
