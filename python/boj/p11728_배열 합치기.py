# input
N, M = map(int, input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = A + B
C.sort()
for e in C:
    print(e,end=' ')