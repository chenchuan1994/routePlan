# Auth: chuan.chen
# Date: 2024-8-19
# Function:
#  不考虑权重到情况下，用深度优先搜索找出所有A-H的路径，以下实现不带回溯

import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from node import edges, get_neighbor
from DFS_STACK.stack import stack

    
'''
1. 初始化栈，将起点名称加到栈顶,栈元素 0-节点名称，1-路径数据
'''
start_node = 'A'
end_node = 'H'

stk = stack()
stk.push([start_node, [start_node]])

'''
2. 初始化一个变量，记录所有的路径
'''
paths = []

'''
3. 深度优先搜索主体逻辑
'''
while not stk.empty():

    curr_node, path = stk.pop()  # 弹出栈顶数据，节点名称，节点列表

    if curr_node == end_node: # 结束条件，走到终点
        paths.append(path)
        continue

    neighbors = get_neighbor(curr_node)  # 找出当前节点的相邻节点

    for n in neighbors:     # 遍历所有相邻的节点
        if n not in path:   # 如果是新节点，将节点添加到路径中
            new_path = path + [n]
            stk.push([n, new_path])  # 新节点数据入栈时，带上路径数据

'''
4. 打印所有路径数据
'''
for path in paths:
    print(path)