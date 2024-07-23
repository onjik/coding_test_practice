# N * M 체스판 왼쪽 아래
# 방문한 칸의 숫자 최대로

# 4보다 많이 움직이려면 한번씩은 사용해야 한다.
# 4보다 많이 움직일 수 있는지 한번 체크

# 4번 다 움직이려면, 적어도 위로 2칸은 있어야 하고
# 오른쪽으로 6칸은 있어야 한다.

# 이 4개를 모두 소모한 경우 (+6, 0) 에 위치한다

# 왼쪽으로 갈 수는 없으므로, 가능하면 위 아래로 두칸 짜리를 사용해야한다
# 사용 할 수 없는 경우에만, 위 아래 한칸 짜리를 사용하자


#  #
#    #
# s
#    #
#  #

n, m = map(int, input().split())
x, y = 0 , n - 1 # x,y 좌표
count = 1
limit = True # 3칸 이상 못 움직임

if m >= 6 and n >= 3:
    # 의무적으로 4개를 사용한다
    x += 6
    count += 4
    limit = False # 제한 해제

# 이제 효율적으로 움직인다.
step_count = 0
if n >= 3: # 세로가 넓은 경우 제일 효율적으로 움직인다
    step_count = m - 1 - x
elif n >= 2: # 2칸인 경우는 차선책을 택한다
    step_count = (m - 1 - x) // 2
else: # 한칸 이하면 아예 못움직인다
    step_count = 0

if limit:
    step_count = min(step_count, 3)

count += step_count

# 이제 count를 출력한다
print(count)



