# 직선, 대각선상에 있으면 안된다.
# N * N 에 N개를 배정하는 것이므로 자료구조는 int[N]을 사용한다.
# int[k] = f 가 의미하는 것은 k번째 줄에 f번째 칸에 배치된다는 것을 의미한다.
# O(N^N) 의 시간복잡도,  Log(15^15) = 17.... 약 2초 정도 예상


# 몇번째 줄 탐색할겨?
def dfs(row):
    global count
    global col_i
    global rb_cross_i
    global lb_cross_i
    if row == N:
        # 탐색 끝났음
        count += 1
        return

    # 쭉 돌면서 가능한 경우 가지치기
    for col in range(N):
        diff = row - col + N -1
        summ = row + col
        # 인덱스 체크해서 가능한지 확인
        if col_i[col] or rb_cross_i[diff] or lb_cross_i[summ]:
            # 이미 존재하는 위치
            continue
        # 가능하므로, 백트래킹
        col_i[col] = True
        rb_cross_i[diff] = True
        lb_cross_i[summ] = True
        dfs(row + 1)
        col_i[col] = False
        rb_cross_i[diff] = False
        lb_cross_i[summ] = False


# input
N = int(input())

# init
count = 0
board = [-1] * N

# 미리 인덱싱을 해놓으면 어떨까?
col_i = [False] * N
rb_cross_i = [False] * (2 * N - 1)  # 2n -1, 차이가 특정 수인 경우
lb_cross_i = [False] * (2 * N - 1)  # 2n -1  합이 특정 수인 경우

# call
dfs(0)

# print
print(count)