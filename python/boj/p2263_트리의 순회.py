# 후위 순회에서 맨 마지막은
# 해당 부분 트리의 루트이다
# 중위 순회에서 루트를 기준으로 양쪽이 왼쪽 부분 트리와 오른쪽 부분트리로 나뉘어진다
import sys
sys.setrecursionlimit(10 ** 5 + 1)
def preorder(in_start, in_end, post_start, post_end):
    if (in_start > in_end) or (post_start > post_end):
        return
    # root 찾기
    root = postorder[post_end]
    print(root, end=' ')

    left_count = index[root] - in_start
    right_count = in_end - index[root]


    # 재귀 호출
    preorder(in_start, in_start + left_count - 1, post_start, post_start + left_count -1)
    preorder(in_end - right_count + 1, in_end, post_end - right_count, post_end - 1)


# input
n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# 인덱스 저장
index = [0] * (n + 1)
for i in range(n):
    index[inorder[i]] = i

preorder(0, n - 1, 0, n - 1)