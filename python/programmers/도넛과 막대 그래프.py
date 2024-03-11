# 정점 갯수 1~
# 단방향 간선
# n개의 정점 n개의 간선
# 도넛 모양 : n개 정점, n개 간선다 돌고 원래 위치로 돌아옴 -> 모든점 다 찍고
# 막대 모양 : n개 정점, n-1개 간선
# 8자 모양 : 2n + 1 개 정점, 2n + 2개 간선 -> 도넛에서 하나를 합친 모습

# 하나의 정점을 생성해서 각 그래프로 가는 간선들 연결
# 그후 각 정점에 서로 다른 번호 매긴다
# 생성된 정점의 번호, 도넛 수, 막대 수, 8자 수

# 10 ** 6

# 들어오는 간선이 없는 점이 생성된 점이다
# 쭉 따라 갈 때, 갈림 길이 없고, 제자리로 돌아올 수 있으면 도넛 형이다
# 쭉 따라 갈 때, 갈림 길이 없고, 막다른 길이 있으면 막대 형이다
# 쭉 따라 갈 때, 갈림 길이 나오면, 8자 형이다

# 특징점을 기준으로 막대와 8자 형을 먼저 세고,
# 생성 노드에서 나가는 엣지 수에서 막대와 8자를 빼자

edge_count = {}


def solution(edges):
    # 입력을 받는다
    for a, b in edges:
        if not edge_count.get(a):
            edge_count[a] = [0, 0]
        if not edge_count.get(b):
            edge_count[b] = [0, 0]
        edge_count[a][0] += 1  # 나가는 것
        edge_count[b][1] += 1  # 들어오는 것

    ans = [0, 0, 0, 0]
    # 특징점을 기준으로 분류한다
    # 8자랑 막대만 일단 센다
    # 시작점을 찾는다
    for key, value in edge_count.items():
        # 막대인지 판별
        if value[0] == 0:
            ans[2] += 1
        # 시작점인지 판별
        elif value[0] > 1 and value[1] == 0:
            ans[0] = key
        # 8자인지 판별
        elif value[0] > 1:
            ans[3] += 1
    # 다 돌았으면, 도넛 수 결정
    ans[1] = edge_count[ans[0]][0] - ans[2] - ans[3]
    return ans