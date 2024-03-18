# 비슷한 문제이다
# 가면서 최대 값을 업데이트 하면서 가자

def update():
    # 초기값은 넣어준다
    memory[0][0] = board[0][0]
    for y in range(1, N):
        for x in range(0, y + 1):
            # 이전 행의 것을 조회한다
            elements = []
            for i in range(x - 1, x + 1):
                if not (0 <= i):
                    continue
                elements.append(memory[y - 1][i])
            prev_max = max(elements)
            memory[y][x] = prev_max + board[y][x]

# 입력을 받아 구성한다
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]

# 부분 최대값을 저장할 배열을 만든다
memory = [[0] * N for _ in range(N)]

# 업데이트를 진행한다
update()

# 맨 마지막 열에서 최대 값을 찾는다
ans = max(memory[-1])

print(ans)

