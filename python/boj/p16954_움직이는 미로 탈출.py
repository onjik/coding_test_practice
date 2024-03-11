# 벽이 맨 아래까지 간다면 사라진다
# 캐릭터가 움직인 후, 벽이 내려가야한다
# 캐릭터가 첫번째 움직임 이후에, 첫번재 줄에 있다면 무조건 성공
# 8번 아래로 내려간다음 생존해 있으면 무조건 성공
# 맵이 움직이므로, visited 체크는 하지 않는다.
# 다만, 벽이랑 겹치는 부분은 제거해야한다.

from collections import deque

# Input
wall_list = list()
for y in range(8):
    row = list(input())
    for x in range(8):
        if row[x] == '#':
            wall_list.append([x, y])

# bfs
q = deque()
q.append((0, 7))
duration = 0
while q:
    for _ in range(len(q)):
        x, y = q.popleft()
        if [x,y] in wall_list:
            continue
        # 성공 체크
        if y == 0 or duration == 7:
            print(1)
            exit()
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                nx = x + dx
                ny = y + dy
                # 맵 밖 체크
                if not (-1 < nx < 8) or not (-1 < ny < 8):
                    continue
                # 벽 체크
                if [nx, ny] in wall_list:
                    continue
                q.append((nx, ny))
    # 벽 아래로 내리기
    wall_list = list(map(lambda coor: [coor[0], coor[1] + 1],wall_list))
    duration += 1
print(0)

# 후기,,
# 문제를 꼼꼼히 완전히 이해하고 풀자