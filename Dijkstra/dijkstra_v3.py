import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from node import edges, get_neighbor, get_cost

all_node = []
for n in edges:
    if n[0] not in all_node: all_node.append(n[0])
    if n[1] not in all_node: all_node.append(n[1])

def get_min_distance_and_node(dis_map: dict):
    distance = float('inf')
    node = None

    for key in dis_map.keys():
        if dis_map[key] < distance:
            distance = dis_map[key]
            node = key
    
    return distance, node


openList = {}   # 存储还没有处理的节点
closeList = {}  # 已经处理过的节点
path = {}

'''
初始化状态
'''
start = 'A'
end = 'H'
openList[start] = 0
path[start] = None

while openList:

    curr_dis, curr_node = get_min_distance_and_node(openList)
    closeList[curr_node] = curr_dis
    openList.pop(curr_node)

    if curr_node == end:
        break

    neighbors = get_neighbor(curr_node)

    for n in neighbors:
        
        if n in closeList:
            continue
        
        acc_cost = get_cost(curr_node, n) + curr_dis

        if n not in openList:
            openList[n] = acc_cost

            # update path data
            if n not in path:
                path[n] = curr_node
            continue

        if openList[n] > acc_cost:
            openList[n] = acc_cost
            path[n] = curr_node

print(path)
print()