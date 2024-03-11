# input
N = int(input())
owneds = list(map(int,input().split()))
M = int(input())
checks = list(map(int,input().split()))

candi = dict()
for owned in owneds:
    if owned in candi:
        candi[owned] += 1
    else:
        candi[owned] = 1

for check in checks:
    if check in candi:
        print(candi[check], end=' ')
    else:
        print(0, end=' ')