# 폴리오미노
# 전체를 백트래킹

MAX = 0
delta = ((1, 0), (0, 1), (-1, 0), (0, -1))


def main():
    # input
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    max_elem = max(map(max, MAP))
    visited = [[False] * M for _ in range(N)]

    def dfs(x, y, block_count, _sum):
        global MAX

        # 블록이 전부 선택되었으면, 종료
        if block_count == 4:
            MAX = max(MAX, _sum)

        # 최대값이 될 가능성이 없으면 조기 종료
        if MAX > _sum + max_elem * (4 - block_count):
            return

        for dx, dy in delta:
            xx = x + dx
            yy = y + dy

            # 맵 이탈 체크
            if not (-1 < xx < M and -1 < yy < N):
                continue
            # 방문 체크
            if visited[yy][xx]:
                continue

            # 방문,
            visited[yy][xx] = True
            dfs(xx, yy, block_count + 1, _sum + MAP[yy][xx])
            if block_count == 2:
                dfs(x, y, block_count + 1, _sum + MAP[yy][xx])
            visited[yy][xx] = False

    # call
    for x in range(M):
        for y in range(N):
            visited[y][x] = True
            dfs(x, y, 1, MAP[y][x])
            visited[y][x] = False

    # print
    print(MAX)


if __name__ == '__main__':
    main()