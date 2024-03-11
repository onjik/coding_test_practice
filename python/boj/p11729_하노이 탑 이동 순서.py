# 하노이 탑을 이동하는 방법
# n -1 만큼 여분 봉으로 이동
# 맨 아래것을 이동
# 다시 n-1만큼 원래 위치로 이동
# 1개 일 때는 무조건 이동

def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return
    hanoi(n - 1, start, 6 - start - end)  # 여분 봉으로 n-1 만큼 이동
    print(start, end)  # 맨 아래거 하나 이동
    hanoi(n - 1, 6 - start - end, end)  # 여분 봉에서 나머지 다이동


# input
N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 3)