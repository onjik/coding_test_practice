# N * N  행렬
# 모두 같지 않으면, 9개로 자른다
# 이걸 몇번 반복해야 하는가
# 재귀 호출로 하면 될 거 같은데

# 함수의 인자는 N, 하고 시작 위치
# 각 숫자로 채워진 종이 갯수

# 처음에 숫자를 다 세 놓고, 거꾸로 올라오면서 숫자를 빼자

# (-1,0,1) 센거 리턴
def count(x, y, n):
    tmp = [0,0,0]
    if n == 1:
        tmp[board[y][x] + 1] = 1
        return tmp
    # 분할해서 호출
    for nx in range(x,x+n,n//3):
        for ny in range(y,y+n,n//3):
            local_count = count(nx,ny,n//3)
            # 합치기
            for i in range(3):
                tmp[i] += local_count[i]
    # 셋중 하나로만 채워져 있으면 하나로 합친다
    if sum(tmp) == 9 and min(tmp) == 0 and max(tmp) == 9: # 정확히 하나만 9인 경우
        for i in range(3):
            if tmp[i] == 9:
                tmp[i] = 1
                break
    return tmp

# input
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
ans = count(0,0,N)
for i in ans:
    print(i)