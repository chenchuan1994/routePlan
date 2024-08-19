import heapq

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from node import edges, get_neighbor, get_cost


# 1. init the cost of all node
cost_map = {}
for e in edges:
    if e[0] not in cost_map:
        cost_map[e[0]] = float('inf')
    if e[1] not in cost_map:
        cost_map[e[1]] = float('inf')


start = 'A'
end = 'H'



min_heap = []

expanded = []



heapq.heappush(min_heap, (0, start))  # 从起点走到这个节点的cost, 节点名字

print(min_heap)

while len(min_heap) != 0:

    curr_cost, curr_node = heapq.heappop(min_heap)

    if curr_node not in expanded:
        expanded.append(curr_node)
    
    if curr_node == end:
        print(expanded)
        break

    neighbors = get_neighbor(curr_node)
    for n in neighbors:
        if cost_map[n] == float('inf') and n not in expanded:
            cost = get_cost(curr_node, n)
            cost_map[n] = curr_cost + cost
            heapq.heappush(min_heap, (cost_map[n], n))
        else:
            cost = get_cost(curr_node, n)
            if cost_map[n] > cost+ curr_cost:
                cost_map[n] = cost + curr_cost
