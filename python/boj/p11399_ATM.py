# input
n = int(input())
p = list(map(int, input().split()))
p.sort()
s = 0
for i, j in zip(p,range(n,0,-1)):
    s += i * j
print(s)