import heapq

graph = {
    '0': {'1': 4, '2': 8},
    '1': {'0': 4, '2': 3, '3': 8},
    '2': {'0': 8, '1': 3, '4': 1, '5': 6},
    '3': {'1': 8, '4': 2, '6': 7, '7': 4},
    '4': {'2': 1, '3': 2, '5': 6},
    '5': {'2': 6, '4': 6, '7': 2},
    '6': {'3': 7, '7': 14, '8': 9},
    '7': {'3': 4, '5': 2, '6': 14, '8': 10},
    '8': {'6': 9, '7': 10}
}

def dijkstra(graph,start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # 初始化父亲节点
    parent = {vertex: None for vertex in graph}
    priority_queue = [(0,start)]

    while priority_queue:
        # 弹出堆中距离最小的节点
        current_distance, current_vertex = heapq.heappop(priority_queue)
        # print("距离最小的节点是:",current_distance, current_vertex, "更新后的队列:",priority_queue)

        # 如果当前距离已经大于已知的最短距离，则跳过
        if current_distance > distances[current_vertex]:
            continue

        # 更新相邻节点的距离
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            # print("相邻节点的距离:",neighbor,distance)

            # 如果找到更短的路径，则更新距离，并将节点加入优先队列
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
                # print("加入后的队列:",priority_queue)
    return distances, parent

distances, parent = dijkstra(graph, '0')
# print(parent)
# print(distances)

# 输出路径回溯
def get_path(parent, start, end):
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path

end_node = '8'
path = get_path(parent, '0', end_node)
print(f"从节点 '0' 到节点 {end_node} 的路径:", path)
