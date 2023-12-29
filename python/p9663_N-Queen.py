# 직선, 대각선상에 있으면 안된다.
# N * N 에 N개를 배정하는 것이므로 자료구조는 int[N]을 사용한다.
# int[k] = f 가 의미하는 것은 k번째 줄에 f번째 칸에 배치된다는 것을 의미한다.
# O(N^N) 의 시간복잡도,  Log(15^15) = 17.... 약 2초 정도 예상

# 몇번째 줄 탐색할겨?
def dfs(row):
    global count
    if row == N:
        # 탐색 끝났음
        count += 1
        return

    # 쭉 돌면서 가능한 경우 가지치기
    for col in range(N):
        # 이 위치가 가능한지 체크
        avaliable = True
        for i in range(row):
            # 대각선과, 직선 체크
            if board[i] == col or abs(i - row) == abs(board[i] - col):
                # 불가능
                avaliable = False
                break
        if avaliable:
            board[row] = col
            dfs(row + 1)


# input
N = int(input())

# init
count = 0
board = [-1] * N

# call
dfs(0)

# print
print(count)