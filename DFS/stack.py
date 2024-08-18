# python 用 list 来模拟栈的行为
# 为了让栈看起来和c++的stack行为比较一致，封装一下
class stack:
    def __init__(self) -> None:
        self._container = []

    def push(self, node: list): # node 结构： 0-节点名称，1-从起点走到当前节点的路径
        """
        数据入栈
        """
        self._container.insert(0, node)

    def pop(self):
        """
        删除并返回栈顶元素
        """
        # node_name = self._container[0]
        return self._container.pop(0)

    def top(self):
        """
        只返回栈顶的元素
        """
        return self._container[0]
    
    def empty(self):
        """
        判断列表是否为空
        """
        if self._container:
            return False
        else:
            return True