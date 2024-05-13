# 플로이드

# n < 100
# m < 100,000
# 모든 도시 쌍에 대해 최단거리 비용
# 매트릭스 형태로 출력

# N값이 작으므로 플로이드 워셜 알고리즘 사용하자
# adj[a][b] = min(adj[a][k] + adj[k][b], adj[a][b])

# 틀렸던 이유
# 1. 자기자신을 향한 간선을 0으로 초기화 안함 -> 플로이드 알고리즘 더 숙달 시키기
# 2. 경로값을 매핑할 때, 최소인지 체크안함(경로 여러개일 수 있다고 했음) -> 문제 잘 읽기
# 3. 맨 마지막에 INF인경우 0으로 바꿔줘야했음 -> 문제 잘 읽기
# input
n = int(input())
m = int(input())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# 일단 초기화
INF = int(1e9)
board = [[INF] * n for _ in range(n)]

for i in range(n):
    board[i][i] = 0

for start, end, cost in edges:
    if cost < board[start -1][end -1]:
        board[start - 1][end - 1] = cost

# 그다음 플로이드 ㄱㄱ
for k in range(n):
    for a in range(n):
        for b in range(n):
            board[a][b] = min(board[a][b], board[a][k] + board[k][b])

for y in range(n):
    for x in range(n):
        if board[y][x] == INF:
            print(0, end=" ")
        else:
            print(board[y][x], end=" ")
    print()
'''
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4

'''