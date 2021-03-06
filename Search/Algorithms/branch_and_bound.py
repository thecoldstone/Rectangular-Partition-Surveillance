from Search.node import *
from Search.guard import *
from time import *


class BranchAndBround:

    def __init__(self, start, nr):

        """
        Least Cost Branch and Bound Algorithm

        :param start: start point
        :param nr: number of rectangles
        """

        self.start = start
        self.nr = nr

    def solve(self, target):

        """

        :param target: in our case target equals number_of_guards >= (number_of_rectangles / 3)
        :return: list of possible guards
        """
        # Lists for open nodes and closed nodes
        q_open = []
        q_close = []

        # Start node
        start_node = Node(self.start, nr=self.nr)

        # Add the start node
        q_open.append(start_node)

        solution = []
        # Upper Bound
        UB = 99999

        while len(q_open) > 0:

            q_open.sort(key=lambda node: node.f and node.nr)

            current_node = q_open.pop(0)
            q_close.append(current_node.location)

            if current_node.nr == 0 and current_node.guard >= target:
                if current_node.guard < UB:
                    UB = current_node.f
                    solution = current_node.get_path
            else:

                possible_guard = get_possible_guard(current_node)
                possible_guard.reverse()

                for i in possible_guard:

                    if i in q_close:
                        continue

                    child = Node(current_node.d, current_node, i)
                    child.nr = child.nr - len(current_node.d[i])
                    delete_rectangles(child.d, child.d[i])

                    for j in range(0, len(q_open) - 1):

                        if q_open[j].location == child.location and q_open[j].f > child.f:
                            q_open.pop(j)

                    if child.f <= UB:
                        q_open.append(child)

        return solution
