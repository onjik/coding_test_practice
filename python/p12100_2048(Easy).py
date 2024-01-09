# 처음에 bfs로 풀었는데 메모리 초과가 떳다
# 블록을 합치는 로직에서 합칠 수 있는 것은 모두 합치도록 로직을 짜서 틀렸었다.
# 예를 들어 16 8 8 0 이 있고 오른쪽으로 민다면
# 0 0 16 16 이렇게 되어야 하는데
# 0 0 0 32 이렇게 되는 식으로 잘못 짯엇다.


def board_view(b):
    l = []
    for i in range(0, N * N, N):
        l.append(b[i:i + N])
    return l


def move_hori(dx):
    global B
    if dx == 1:  # 오른쪽으로 움직인다, 오른쪽 부터 스캔
        scan_order = range(N - 1, -1, -1)
    else:  # 왼쪽으로 움직인다, 왼쪽부터 스캔
        scan_order = range(0, N, 1)
    tmp = [0] * N * N
    for y in range(N):
        st = []
        for x in scan_order:
            v = B[x + y * N]
            if v == 0:
                continue
            st.append(v)
        # 블록 합쳐짐 처리
        idx = 0
        while idx + 1 < len(st):
            if st[idx] == st[idx + 1]:
                st[idx] *= 2
                st.pop(idx + 1)
            idx += 1
        # 만들어 진 녀석을 추가한다
        for i, v in enumerate(st):
            tmp[scan_order[i] + y * N] = v
    B = tmp


def move_verti(dy):
    global B
    if dy == 1:  # 오른쪽으로 움직인다, 오른쪽 부터 스캔
        scan_order = range(N - 1, -1, -1)
    else:  # 왼쪽으로 움직인다, 왼쪽부터 스캔
        scan_order = range(0, N, 1)
    tmp = [0] * N * N
    for x in range(N):
        st = []
        for y in scan_order:
            v = B[x + y * N]
            if v == 0:
                continue
            st.append(v)
        # 블록 합쳐짐 처리
        idx = 0
        while idx + 1 < len(st):
            if st[idx] == st[idx + 1]:
                st[idx] *= 2
                st.pop(idx + 1)
            idx += 1

        # 만들어 진 녀석을 추가한다
        for i, v in enumerate(st):
            tmp[x + scan_order[i] * N] = v
    B = tmp

def refresh_max():
    global ans
    ans = max(max(B), ans)


# step은 0 부터
def dfs(step):
    global B
    if step == 5:
        refresh_max()
        return

    bc = B.copy()

    for i in [1, -1]:
        move_verti(i)
        if B != bc:
            dfs(step + 1)
            B = bc.copy()
        else:
            refresh_max()
        move_hori(i)
        if B != bc:
            dfs(step + 1)
            B = bc.copy()
        else:
            refresh_max()

# 아래로 한칸, 우로 한칸, 위로 한, 위로 한칸, 우로 한칸
N = int(input())
B = []
for _ in range(N):
    B += list(map(int, input().split()))
ans = -1
dfs(0)
print(ans)
