import sys


# 현재 위치에서 저 위치에 도착하는데 최소 주사위 던지는 횟수
# 사다리 밟지 않고
# bfs
def min_throw(current_pos, dest_pos):
    count = 0
    q = []
    q.append(current_pos)

    while q:
        count += 1
        for _ in range(len(q)):
            pos = q.pop(0)
            # 목적지까지 6칸 이내면, 조기 종료
            if dest_pos - pos <= 6:
                return count  # 종료 조건
            for i in range(6, 0, -1):
                # 사다리 칸이면, 무조건 거부
                np = pos + i
                if np in LI:
                    continue
                # 일반 칸이면, 이동
                q.append(np)
                break
    # 여기 까지 왔으면, 절대 못가는거
    return -1


def dfs(count, pos):
    global ans
    if count > ans:
        return
    f = list(filter(lambda x: x[0] > pos and not (x in visited), L))

    # 링크 이용을 안하는 경우
    # 100까지 직진하라는 말
    d = min_throw(pos, 100)
    if d != -1:  # -1이면 절대 못가는거
        ans = min(ans, count + min_throw(pos, 100))

    for link in f:
        # 저기로 이동한다는 뜻
        d = min_throw(pos, link[0])
        if d == -1:
            continue
        visited.add(link)
        dfs(count + d, link[1])
        visited.remove(link)


# input
N, M = map(int, input().split())

L = [tuple(map(int, input().split())) for _ in range(N + M)]
LI = set()
for i in L:
    LI.add(i[0])

ans = sys.maxsize
visited = set()

dfs(0, 1)
print(ans)
