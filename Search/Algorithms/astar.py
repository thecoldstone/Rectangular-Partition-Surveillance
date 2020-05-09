from Search.node import *
from Search.guard import *
from time import *

class AStar:

    def __init__(self, start, nr):
        self.start = start
        self.nr = nr

    def solve(self, target):
        # Lists for open nodes and closed nodes
        q_open = []
        q_close = []

        # Start node
        start_node = Node(self.start, nr=self.nr)

        # Add the start node
        q_open.append(start_node)

        while len(q_open) > 0:


            q_open.sort(key=lambda node: node.f)

            # for i in q_open:
            #     print(i.location, i.f, ';', end='')
            # print()
            current_node = q_open.pop(0)

            q_close.append(current_node)

            if current_node.nr == 0 and current_node.guard >= target:
                return current_node.get_path

            possible_guard = get_possible_guard(current_node)

            if possible_guard is None:
                continue

            children = []
            for i in possible_guard:
                child = Node(current_node.d, current_node, i)
                child.nr = child.nr - len(current_node.d[i])
                delete_rectangles(child.d, child.d[i])
                children.append(child)

            for child in children:

                # if child.parent is not None:
                #     print(child.parent.location, end='')
                #     print('->'*child.guard, end='')
                #     print(child.location, end='')
                # sleep(1)
                if child in q_close:
                    continue

                for open_node in q_open:
                    if child == open_node and child.g > open_node.g:
                        continue

                q_open.append(child)

        return []
