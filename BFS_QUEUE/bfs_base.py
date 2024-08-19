import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from node import edges, get_neighbor
import queue

start = "A"
end = "H"

node_queue = queue.Queue()
node_queue.put(start)

path_queue = queue.Queue()
path_queue.put([start])

while not node_queue.empty():

    curr_node = node_queue.get()
    curr_path = path_queue.get()

    print(curr_node)

    if end == curr_node:
        print(curr_path)

    neighbors = get_neighbor(curr_node)
    for n in neighbors:
        if n not in curr_path:
            node_queue.put(n)
            path_queue.put(curr_path + [n])