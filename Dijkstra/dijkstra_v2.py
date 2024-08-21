import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from node import edges, get_neighbor, get_cost

all_node = []
for n in edges:
    if n[0] not in all_node: all_node.append(n[0])
    if n[1] not in all_node: all_node.append(n[1])

print(all_node)

kwon = []   # 如果节点被处理过了，不再进行处理
distance_map = {}
pre_node_map = {}

'''
初始化状态
'''
start_node = 'A'
end_node = 'D'

distance_map[start_node] = 0     # 充当最小堆
pre_node_map[start_node] = None  # 用来还原路径

def get_min_distance_and_node(dis_map: dict):
    distance = float('inf')
    node = None

    for key in dis_map.keys():
        if dis_map[key] < distance:
            distance = dis_map[key]
            node = key
    
    return distance, node

while distance_map:

    curr_dis, curr_node = get_min_distance_and_node(distance_map)
    distance_map.pop(curr_node)
    kwon.append(curr_node)

    if curr_node == end_node:
        print(curr_dis, curr_node)
        break

    neighbors = get_neighbor(curr_node)
    for n in neighbors:

        if n in kwon:
            continue

        acc_dis = curr_dis + get_cost(curr_node, n)

        if n not in distance_map:
            distance_map[n] = acc_dis
            pre_node_map[n] = curr_node

        elif distance_map[n] > acc_dis:
            distance_map[n] = acc_dis
            pre_node_map[n] = curr_node
        else:
            pass
        

# 还原path
node = pre_node_map[end_node]
path = [end_node]

while node:
    path.append(node)
    node = pre_node_map[node]

path.reverse()
print(path)

'''
总结：
这个版本不好的地方是，distance_map 中预先放了所有的节点，但实际上应该是有限扩展
'''