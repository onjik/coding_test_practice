# 완탐 하는 문제 이다.
# 2초이고, T의 길이가 50으로 짧다는 것에서 눈치를 챘어야 했다.

# input
s = input()
t = input()
s_len = len(s)

def dfs(word):
    """s와 같으면 종료"""
    if word == s:
        print(1)
        exit()
    if len(word) == s_len:
        return
    if word[-1] == "A":
        dfs(word[:-1])
    if word[0] == "B":
        dfs(word[1:][::-1])

dfs(t)
print(0)