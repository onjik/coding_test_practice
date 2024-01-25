# 한마리의 고슴도치 -> 굴
# R 행 C 열
# 빈칸 . 물 * 돌 X 굴 D 고슴도치 S
# 인접 4칸 이동가능
# 매 step 마다 물이 인접한 곳으로 번짐
# 물과 고슴도치는 돌 통과할 수 없다
# 고슴도치는 물로 갈 수 없다.
# 물은 굴로 갈 수 없다
# 최소시간
# 고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다(다음번에 물이 찰 곳으로 이동하면 빠져 죽음)
# 물이 먼저 번지고, 고슴도치를 움직이도록
# 고슴도치를 Pop 했을 때 현재 위치가 물인지를 한번 더 확인
# 고슴도치 움직이고, 물 번지고, 고슴도치 꺼낼 때 한번 더 체크
# 이동할 수 없다면, KAKTUS

# bfs 사용하자
# visited 체크를 하자, 어차피 물이 번지면 갈 수 있는 갈래길이 줄어들기만 하므로

from collections import deque


def water_raise():
    global board
    # 물인 공간 다 넣기
    waters = []
    for y in range(R):
        for x in range(C):
            if board[y][x] == '*':
                waters.append([x, y])
    # 순차적으로 꺼내면서 번지게 하기
    for water in waters:
        wx, wy = water[0], water[1]
        for i in range(4):
            wnx = wx + dx[i]
            wny = wy + dy[i]
            # 맵 밖 체크
            if not (-1 < wnx < C) or not (-1 < wny < R):
                continue
            # 이미 물이거나 돌이거나 굴이면
            if board[wny][wnx] == '*' or board[wny][wnx] == 'X' or board[wny][wnx] == 'D':
                continue
            # 물로 색칠하기
            board[wny][wnx] = '*'


# input
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
s_pos = (-1, -1)
for y in range(R):
    for x in range(C):
        if board[y][x] == 'S':
            s_pos = (x, y)
            break
    if s_pos != (-1, -1):
        break

# bfs
q = deque()
visited = [[False] * C for _ in range(R)]
q.append(s_pos)
visited[s_pos[1]][s_pos[0]] = True

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

step = 0
while q:
    for _ in range(len(q)):
        x, y = q.popleft()
        # 물 체크
        if board[y][x] == '*':
            continue
        # 정답 체크
        if board[y][x] == 'D':
            print(step)
            exit()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 맵 체크
            if not (-1 < nx < C) or not (-1 < ny < R):
                continue
            # visited 체크
            if visited[ny][nx]:
                continue
            # 물, 돌 체크
            if board[ny][nx] == '*' or board[ny][nx] == 'X':
                continue
            # 진행
            visited[ny][nx] = True
            q.append((nx, ny))
    # 한개의 step이 모두 진행 했으면,
    step += 1
    # 물 번지게 하기
    water_raise()

# 여기까지 왔으면, 못가는 거임
print("KAKTUS")