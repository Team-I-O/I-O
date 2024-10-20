import random as rd

landmark = {0: None, 1: 'road', 2: 'shop', 3: 'treasure', 4: 'boss', 5: 'forbidden'}
def mapping():
    dungeon = [[0 for _ in range(5)]for _ in range(5)]

    landmark_pos = ((rd.randint(0, 4), rd.randint(0, 4), mark)for mark in rd.sample([3, 4, 5], 3))  # 위치 중복 없게 수정 필요

    dungeon[2][2] = 1
    corner = [0, 4]
    zone = {2: None, 3: None, 4: None}

    def random_map():
        while 1:
            x, y = rd.randint(0, 4), rd.randint(0, 4)

            if x in corner and y in corner:
                if x == 0 and ((dungeon[1][y] == 0) and (dungeon[2][y] == 0)):
                    return x, y
                elif x == 4 and ((dungeon[4][y] == 0) and (dungeon[3][y] == 0)):
                    return x, y
                elif y == 0 and ((dungeon[x][1] == 0) and (dungeon[x][2] == 0)):
                    return x, y
                elif y == 4 and ((dungeon[x][4] == 0) and (dungeon[x][3] == 0)):
                    return x, y
            elif dungeon[x][y] == 0 and ((x == 0 or x == 4) or (y == 0 or y == 4)):  # 중복 및 테두리 부분 나올 때 까지 랜덤 돌리기
                return x, y

    for x, y in landmark_pos:
        if dungeon[x][y] >= 1 or ((x != 0 or x != 4) and (y != 0 or y != 4)):  # 금지 구역을 생성 못할 경우 다시 돌리기
            x, y = random_map()

        elif x in corner and y in corner:
            if x == 0 and ((dungeon[1][y] != 0) or (dungeon[2][y] != 0)):
                x, y = random_map()
            elif x == 4 and ((dungeon[4][y] != 0) or (dungeon[3][y] != 0)):
                x, y = random_map()
            elif y == 0 and ((dungeon[x][1] != 0) or (dungeon[x][2] != 0)):
                x, y = random_map()
            elif y == 4 and ((dungeon[x][4] != 0) or (dungeon[x][3] != 0)):
                x, y = random_map()

        if (x in corner) and (y in corner):  # 금지 구역 생성
            if x == 0:
                dungeon[x + 1][y] = 5
                dungeon[x + 2][y] = 5
            elif x == 4:
                dungeon[x - 1][y] = 5
                dungeon[x - 2][y] = 5

            if y == 0:
                dungeon[x][y + 1] = 5
                dungeon[x][y + 2] = 5
            elif y == 4:
                dungeon[x][y - 1] = 5
                dungeon[x][y - 2] = 5

        else:
            if x == 0 or x == 4:
                dungeon[x][y + 1] = 5
                dungeon[x][y - 1] = 5
            elif x >= 3:
                dungeon[x + 1][y] = 5
                dungeon[x - 1][y] = 5

        if zone[2] == None:
            zone[2] = (x, y)
            dungeon[x][y] = 2
        elif zone[3] == None:
            zone[3] = (x, y)
            dungeon[x][y] = 3
        else:
            zone[4] = (x, y)
            dungeon[x][y] = 4

    for x, y, m in landmark_pos:
        dungeon[x][y] = m
        pos_x = 2
        pos_y = 2
        dir_x = 0
        dir_y = 0


        if x-2 > 0:
            dir_x = 1
        elif x-2 < 0:
            dir_x = -1
        if y-2 > 0:
            dir_y = 1
        if y-2 < 0:
            dir_y = -1
        while 1:
            pos_x += dir_x
            dungeon[pos_x][pos_y] = 1
            if dungeon[pos_x+dir_x][pos_y] == m:
                break
            elif dungeon[pos_x][pos_y+dir_y] == m:
                break
            pos_y += dir_y
            dungeon[pos_x][pos_y] = 1
            if dungeon[pos_x+dir_x][pos_y] == m:
                break
            elif dungeon[pos_x][pos_y+dir_y] == m:
                break


    return dungeon

print(mapping())

'''
 나의 생각은...
 마지막 길의 위치에서 상,하,좌,우 중 하나로 이동해서
 그 위치가 자신이 생성했던 길(=road)의 상,하,좌,우 (단, 바로 전의 길 제외)이라면 취소하고, 맞으면 저장하는 것을 랜덤하게 반복하기
 => 이차원 리스트..?
 + 마지막 위치 에서 시작점까지 역추적하기(랜덤?)
 
 5*5 공간이라서 크게 경로 중요 X
 => 테두리 따라 랜드마크 랜덤 선택(단, 랜드마크의 상,하,좌,우에 다른 랜드마크 X), 도시로 역추적
'''

# PQ.push(start_node, g(start_node) + h(start_node))       //우선순위 큐에 시작 노드를 삽입한다.
#
# while PQ is not empty       //우선순위 큐가 비어있지 않은 동안
#     node = PQ.pop       //우선순위 큐를 pop한다.
#
#     if node == goal_node       //만일 해당 노드가 목표 노드이면 반복문을 빠져나온다.
#         break
#
#     for next_node in (next_node_begin...next_node_end)       //해당 노드에서 이동할 수 있는 다음 노드들을 보는 동안
#         PQ.push(next_node, g(node) + cost + h(next_node))       //우선순위 큐에 다음 노드를 삽입한다.
#
# print goal_node_dist       //시작 노드에서 목표 노드까지의 거리를 출력한다.


