'''
带回溯版本的dfs
用stack的回溯是数据不出栈, 能从H直接跳到D的回溯
'''

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from node import edges, get_neighbor
from DFS_STACK.stack import stack

# 1.确定起点终点，初始化栈对象，将起点作为第一个元素入栈
start = 'A'
end = 'H'

node_stk = stack()
node_stk.push(start)

path_stk = stack()  # 存储走到当前节点累积的路径
path_stk.push([start])

paths = []

while not node_stk.empty():

    curr_node = node_stk.pop()   # 弹出栈顶元素
    curr_path = path_stk.pop()

    print(curr_node)

    if curr_node == end:
        paths.append(curr_path)
        # print(curr_path)
        continue

    neighbors = get_neighbor(curr_node)

    for n in neighbors:   # 这实际是bfs
        if n not in curr_path:
            node_stk.push(n)   
            path_stk.push(curr_path + [n])
            
for p in paths:
    print(p)
