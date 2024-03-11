# input
N = int(input())
owneds = list(map(int,input().split()))
M = int(input())
checks = list(map(int,input().split()))

candi = set()
for owned in owneds:
    candi.add(owned)

for check in checks:
    if check in candi:
        print(1, end=' ')
    else:
        print(0, end=' ')