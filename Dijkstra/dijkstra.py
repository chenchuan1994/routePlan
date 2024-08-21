import heapq

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from node import edges, get_neighbor, get_cost

all_node = []
for n in edges:
    if n[0] not in all_node: all_node.append(n[0])
    if n[1] not in all_node: all_node.append(n[1])

print(all_node)

'''
Init status
'''
cost_map = {n : float('inf') for n in all_node}
pre_node = {n:None for n in all_node}
kwon = {n:0 for n in all_node}
expanded = {n:0 for n in all_node}
min_heap = []  # (accumulate_cost, node_name)
at_heap = []

start_node = "A"
cost_map[start_node] = 0
heapq.heappush(min_heap, [cost_map[start_node], start_node])

end_node = "H"

while min_heap:

    curr_cost, curr_node = heapq.heappop(min_heap)  # 取出当前累积cost最小的节点

    if curr_node == end_node:
        break

    neighbors = get_neighbor(curr_node)

    for n in neighbors:
        acc_cost = get_cost(curr_node, n) + curr_cost  # 计算累积cost + 走到n的cost

        if expanded[n] == 0:  # 还没有被扩展，放到最小堆中
            heapq.heappush(min_heap, [acc_cost, n])
            pre_node[n] = curr_node
            expanded[n] = 1
        else:
            for item in min_heap:
                if item[1] == n and item[0] > acc_cost:
                    item[0] = acc_cost
                    pre_node[n] = curr_node


node = end_node
path = [node]

pre = pre_node[node]

while pre:

    path.append(pre)

    if pre == start_node:
        break
    
    pre = pre_node[pre]

path.reverse()
print(path)